const N: usize = 5;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

struct CarryIn {
    aaa: Vec<Vec<usize>>,
    index: Vec<usize>,
}

impl CarryIn {
    fn read() -> CarryIn {
        read_line();

        let mut aaa = vec![];
        for _ in 0..N {
            aaa.push(read_vec());
        }

        CarryIn { aaa, index: vec![0; N] }
    }

    fn from(aaa: &Vec<Vec<usize>>) -> CarryIn {
        CarryIn {
            aaa: aaa.clone(),
            index: vec![0; N],
        }
    }

    fn peek(&self, row: usize) -> Option<usize> {
        self.aaa[row].get(self.index[row]).cloned()
    }

    fn pop(&mut self, row: usize) -> Option<usize> {
        let ret = self.peek(row);
        if ret.is_some() {
            self.index[row] += 1;
        }
        ret
    }
}

struct CarryOut {
    aaa: Vec<Vec<usize>>,
    sum: usize,
}

impl CarryOut {
    fn new() -> CarryOut {
        CarryOut { aaa: vec![vec![]; N], sum: 0 }
    }

    fn push(&mut self, row: usize, container_id: usize) {
        self.aaa[row].push(container_id);
        self.sum += 1;
    }

    fn score(&self) -> (usize, (usize, usize, usize)) {
        let mut m1 = 0;
        let mut m2 = 0;
        for row in 0..N {
            let aa = &self.aaa[row];
            let mut bb = vec![];

            for &a in aa {
                if row * N <= a && a < row * N + N {
                    bb.push(a);
                }
            }
            m2 += aa.len() - bb.len();

            for i in 0..bb.len() {
                for j in i + 1..bb.len() {
                    if bb[i] > bb[j] {
                        m1 += 1;
                    }
                }
            }
        }

        let m3 = N * N - self.sum;

        (m1 * 100 + m2 * 10_000 + m3 * 1_000_000, (m1, m2, m3))
    }
}

#[derive(Clone, Debug, Copy)]
struct Coord(usize, usize);

impl Coord {
    fn is_top_edge(&self) -> bool {
        self.0 == 0
    }

    fn is_bottom_edge(&self) -> bool {
        self.0 == N - 1
    }

    fn is_left_edge(&self) -> bool {
        self.1 == 0
    }

    fn is_right_edge(&self) -> bool {
        self.1 == N - 1
    }

    fn up(&self) -> Option<Coord> {
        if self.is_top_edge() {
            None
        } else {
            Some(Coord(self.0 - 1, self.1))
        }
    }

    fn down(&self) -> Option<Coord> {
        if self.is_bottom_edge() {
            None
        } else {
            Some(Coord(self.0 + 1, self.1))
        }
    }

    fn left(&self) -> Option<Coord> {
        if self.is_left_edge() {
            None
        } else {
            Some(Coord(self.0, self.1 - 1))
        }
    }

    fn right(&self) -> Option<Coord> {
        if self.is_right_edge() {
            None
        } else {
            Some(Coord(self.0, self.1 + 1))
        }
    }
}

#[derive(Clone)]
struct Cell {
    coord: Coord,
    crane_id: Option<usize>,
    crane_grab: Option<bool>,
    container_id: Option<usize>,
    lifted_container_id: Option<usize>,
}

impl Cell {
    fn grab(&mut self) {
        if self.crane_id.is_none() {
            panic!("grab error 1");
        }
        if !self.crane_grab.is_some_and(|v| v == false) {
            panic!("grab error 2");
        }
        if self.container_id.is_none() {
            panic!("grab error 3");
        }

        self.crane_grab = Some(true);
        if self.crane_id.unwrap() == 0 {
            self.lifted_container_id = self.container_id;
            self.container_id = None;
        }
    }

    fn ungrab(&mut self) {
        if self.crane_id.is_none() {
            panic!("ungrab error 1");
        }
        if !self.crane_grab.is_some_and(|v| v == true) {
            panic!("ungrab error 2");
        }

        self.crane_grab = Some(false);
        if self.crane_id.unwrap() == 0 {
            self.container_id = self.lifted_container_id;
            self.lifted_container_id = None;
        }
    }

    fn go_out(&mut self) {
        if self.crane_id.is_none() {
            panic!("go_out error 1");
        }
        let crane_id = self.crane_id.unwrap();
        let grab = self.crane_grab.unwrap();

        if grab {
            if crane_id == 0 {
                self.lifted_container_id = None;
            } else {
                self.container_id = None;
            }
        }
        self.crane_id = None;
        self.crane_grab = None;
    }

    fn go_in(&mut self, from: &Cell) {
        if self.crane_id.is_some() {
            panic!("go_in error 1");
        }
        let crane_id = from.crane_id.unwrap();
        let grab = from.crane_grab.unwrap();

        if grab {
            if crane_id == 0 {
                self.lifted_container_id = from.lifted_container_id;
            } else {
                self.container_id = from.container_id;
            }
        }
        self.crane_id = from.crane_id;
        self.crane_grab = from.crane_grab;
    }
}

#[derive(Clone)]
struct Board(Vec<Cell>);

impl Board {
    fn new() -> Board {
        let mut cells = vec![];
        for row in 0..N {
            for col in 0..N {
                let crane_id = if col == 0 { Some(row) } else { None };
                let crane_grab = if col == 0 { Some(false) } else { None };

                let cell = Cell {
                    coord: Coord(row, col),
                    crane_id,
                    crane_grab,
                    container_id: None,
                    lifted_container_id: None,
                };
                cells.push(cell);
            }
        }

        Board(cells)
    }

    fn at(&self, coord: Coord) -> &Cell {
        let Coord(row, col) = coord;
        &self.0[row * N + col]
    }

    fn at_mut(&mut self, coord: Coord) -> &mut Cell {
        let Coord(row, col) = coord;
        &mut self.0[row * N + col]
    }

    fn get_crane_cell(&self, crane_id: usize) -> Option<&Cell> {
        for row in 0..N {
            for col in 0..N {
                let cell = self.at(Coord(row, col));
                if cell.crane_id.is_some_and(|v| v == crane_id) {
                    return Some(cell);
                }
            }
        }
        None
    }

    fn put(&mut self, coord: Coord, container_id_or_none: Option<usize>) {
        let Coord(row, col) = coord;
        self.0[row * N + col].container_id = container_id_or_none;
    }

    fn apply_move(&self, moves: &Vec<MoveType>) -> Board {
        let mut new_board = self.clone();

        for crane_id in 0..N {
            let moveType = moves[crane_id];

            let cur_cell = self.get_crane_cell(crane_id);
            if cur_cell.is_none() {
                continue;
            }
            let cur_cell = cur_cell.unwrap();
            let cur_coord = cur_cell.coord;

            if moveType == Grab {
                new_board.at_mut(cur_coord).grab();
            }

            if moveType == UnGrab {
                new_board.at_mut(cur_coord).ungrab();
            }

            if moveType == MoveRight {
                new_board.at_mut(cur_coord).go_out();
            }

            if moveType == MoveLeft {
                new_board.at_mut(cur_coord).go_out();
            }
        }

        for crane_id in 0..N {
            let moveType = moves[crane_id];

            let cur_cell = self.get_crane_cell(crane_id);
            if cur_cell.is_none() {
                continue;
            }
            let cur_cell = cur_cell.unwrap();
            let cur_coord = cur_cell.coord;

            if moveType == MoveRight {
                new_board.at_mut(cur_coord.right().unwrap()).go_in(cur_cell);
            }

            if moveType == MoveLeft {
                new_board.at_mut(cur_coord.left().unwrap()).go_in(cur_cell);
            }
        }

        new_board
    }
}

struct Game {
    turn: usize,
    board: Board,
    carry_in: CarryIn,
    carry_out: CarryOut,
    moves_history: Vec<Vec<MoveType>>,
}

impl Game {
    fn from(carry_in: CarryIn) -> Game {
        Game {
            turn: 0,
            board: Board::new(),
            carry_in,
            carry_out: CarryOut::new(),
            moves_history: vec![],
        }
    }

    fn carry_in(&mut self) {
        for row in 0..N {
            let coord = Coord(row, 0);
            let cell = self.board.at(coord);
            if cell.container_id.is_none() && cell.lifted_container_id.is_none() {
                let container_id = self.carry_in.pop(row);
                self.board.put(coord, container_id);
            }
        }
    }

    fn carry_out(&mut self) {
        for row in 0..N {
            let coord = Coord(row, N - 1);
            let cell = self.board.at(coord);
            if let Some(container_id) = cell.container_id {
                if !cell.crane_grab.is_some_and(|v| v) || cell.crane_id.is_some_and(|v| v == 0) {
                    self.carry_out.push(row, container_id);
                    self.board.put(coord, None);
                }
            }
        }
        self.turn += 1;
    }

    fn r#move(&mut self, strategy: &Strategy) {
        let mut moves = vec![Skip; N];
        for crane_id in 0..N {
            let cell = self.board.get_crane_cell(crane_id);
            if cell.is_none() {
                continue;
            }
            let cell = cell.unwrap();
            let coord = cell.coord;

            if coord.is_left_edge() && !cell.crane_grab.unwrap() {
                moves[crane_id] = Grab;
            }

            if !coord.is_right_edge() && cell.crane_grab.unwrap() {
                moves[crane_id] = MoveRight;
            }

            if coord.is_right_edge() && cell.crane_grab.unwrap() {
                moves[crane_id] = UnGrab;
            }

            if !coord.is_left_edge() && !cell.crane_grab.unwrap() {
                moves[crane_id] = MoveLeft;
            }
        }

        // println!("{moves:?}");

        self.moves_history.push(moves.clone());
        self.board = self.board.apply_move(&moves);
    }

    fn finished(&self) -> bool {
        self.turn == 10000 || self.carry_out.sum == N * N
    }

    fn score(&self) -> (usize, (usize, usize, usize, usize)) {
        let m0 = self.turn;
        let (score_co, (m1, m2, m3)) = self.carry_out.score();
        (self.turn + score_co, (m0, m1, m2, m3))
    }

    fn print_ans(&self) {
        for crane_id in 0..N {
            let mut moves = vec![];
            for hist in &self.moves_history {
                moves.push(hist[crane_id]);
            }
            println!("{}", moves_str(&moves));
        }
    }
}

#[derive(Clone, Copy, PartialEq, Debug)]
enum MoveType {
    Grab,
    UnGrab,
    MoveLeft,
    MoveRight,
    MoveUp,
    MoveDown,
    Skip,
    Bang,
}
use MoveType::*;

fn moves_str(moves: &Vec<MoveType>) -> String {
    let mut ss = vec![];
    for moveType in moves {
        ss.push(match moveType {
            Grab => "P",
            UnGrab => "Q",
            MoveLeft => "L",
            MoveRight => "R",
            MoveUp => "U",
            MoveDown => "D",
            Skip => ".",
            Bang => "B",
        })
    }
    ss.join("")
}

use std::fmt::{Display, Error, Formatter};
impl Display for Game {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error> {
        writeln!(f, "Game [turn: {}]", self.turn);

        let carry_in = &self.carry_in;

        for row in 0..N {
            let carry_in = (0..N).rev().map(|i| {
                if carry_in.index[row] <= i {
                    format!(" {:>2} ", &carry_in.aaa[row][i])
                } else {
                    format!("({:>2})", &carry_in.aaa[row][i])
                }
            });
            let carry_in = carry_in.collect::<Vec<_>>().join(" ");

            let mut cells = vec![];
            for col in 0..N {
                let cell = &self.board.at(Coord(row, col));

                let crane = cell.crane_id.map_or(" ".to_string(), |v| v.to_string());

                let grab = match cell.crane_grab {
                    Some(true) => "=",
                    Some(false) => ".",
                    _ => " ",
                };

                let lifted_con = cell.lifted_container_id.map_or("   ".to_string(), |v| format!("{v:>2},"));
                let con = cell.container_id.map_or("".to_string(), |v| v.to_string());

                cells.push(format!("[{crane}{grab}{lifted_con}{con:>2}]"));
            }
            let cells = cells.join(" ");

            let mut carry_out = vec![];
            for &con in &self.carry_out.aaa[row] {
                let in_range = row * N <= con && con < row * N + N;
                let s = if in_range { format!(" {con:>2} ") } else { format!("({con:>2})") };
                carry_out.push(s);
            }
            let carry_out = carry_out.join(" ");

            writeln!(f, "{carry_in} {cells} {carry_out}");
        }

        write!(f, "")
    }
}

struct Strategy;

impl Strategy {}

fn main() {
    let mut carry_in = CarryIn::read();
    let mut game = Game::from(carry_in);

    let strategy = Strategy;

    while !game.finished() {
        game.carry_in();
        game.r#move(&strategy);
        game.carry_out();

        // eprintln!("{game}");
    }

    // eprintln!("{:?}", game.score());
    game.print_ans();
}
