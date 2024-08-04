const N: usize = 5;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

#[derive(Clone)]
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
    cnt: Vec<usize>,
}

impl CarryOut {
    fn new() -> CarryOut {
        CarryOut {
            aaa: vec![vec![]; N],
            sum: 0,
            cnt: vec![0; N],
        }
    }

    fn push(&mut self, row: usize, container_id: usize) {
        self.aaa[row].push(container_id);
        self.sum += 1;
        self.cnt[row] += 1;
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

#[derive(Clone, Debug, Copy, PartialEq)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}
use Direction::*;

#[derive(Clone, Debug, Copy)]
struct Coord(usize, usize);

impl Coord {
    fn row(&self) -> usize {
        self.0
    }
    fn col(&self) -> usize {
        self.1
    }

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

    fn step(&self, dir: Direction) -> Option<Coord> {
        match dir {
            Up => self.up(),
            Down => self.down(),
            Left => self.left(),
            Right => self.right(),
        }
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

    fn approach(&self, dest: Coord, horizontal: bool) -> Option<Direction> {
        if horizontal {
            if self.col() < dest.col() {
                return Some(Right);
            }
            if self.col() > dest.col() {
                return Some(Left);
            }
        }

        if self.row() < dest.row() {
            return Some(Down);
        }
        if self.row() > dest.row() {
            return Some(Up);
        }
        if self.col() < dest.col() {
            return Some(Right);
        }
        if self.col() > dest.col() {
            return Some(Left);
        }

        None
    }

    fn dist(&self, dest: Coord) -> usize {
        let dx = (self.row() as i64 - dest.row() as i64).abs() as usize;
        let dy = (self.col() as i64 - dest.col() as i64).abs() as usize;
        dx + dy
    }
}

#[derive(Clone, Debug)]
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

    fn bang(&mut self) {
        if self.crane_id.is_none() {
            panic!("bang error 1");
        }
        if self.crane_grab.is_some_and(|v| v == true) {
            panic!("bang error 2");
        }

        self.crane_id = None;
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

    fn get_container_cell(&self, container_id: usize) -> Option<&Cell> {
        for row in 0..N {
            for col in 0..N {
                let cell = self.at(Coord(row, col));
                if cell.container_id.is_some_and(|v| v == container_id) {
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
            let move_type = moves[crane_id];

            let cur_cell = self.get_crane_cell(crane_id);
            if cur_cell.is_none() {
                continue;
            }
            let cur_cell = cur_cell.unwrap();
            let cur_coord = cur_cell.coord;

            if move_type == Grab {
                new_board.at_mut(cur_coord).grab();
            }

            if move_type == UnGrab {
                new_board.at_mut(cur_coord).ungrab();
            }

            if move_type == Bang {
                new_board.at_mut(cur_coord).bang();
            }

            if let Move(_) = move_type {
                new_board.at_mut(cur_coord).go_out();
            }
        }

        for crane_id in 0..N {
            let move_type = moves[crane_id];

            let cur_cell = self.get_crane_cell(crane_id);
            if cur_cell.is_none() {
                continue;
            }
            let cur_cell = cur_cell.unwrap();
            let cur_coord = cur_cell.coord;

            if let Move(dir) = move_type {
                let new_coord = cur_coord.step(dir).unwrap();
                new_board.at_mut(new_coord).go_in(cur_cell);
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

    fn r#move<TStrategy: Strategy>(&mut self, strategy: &mut TStrategy) {
        let moves = strategy.next_moves(self);

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
    Move(Direction),
    Skip,
    Bang,
}
use MoveType::*;

fn moves_str(moves: &Vec<MoveType>) -> String {
    let mut ss = vec![];
    for move_type in moves {
        ss.push(match move_type {
            Grab => "P",
            UnGrab => "Q",
            Move(Left) => "L",
            Move(Right) => "R",
            Move(Up) => "U",
            Move(Down) => "D",
            Skip => ".",
            Bang => "B",
        })
    }
    ss.join("")
}

use std::fmt::{Display, Error, Formatter};
impl Display for Game {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error> {
        writeln!(f, "Game [turn: {}]", self.turn)?;

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

            writeln!(f, "{carry_in} {cells} {carry_out}")?;
        }

        write!(f, "")
    }
}

trait Strategy {
    fn next_moves(&mut self, game: &Game) -> Vec<MoveType>;
}

struct Strategy1;
impl Strategy for Strategy1 {
    fn next_moves(&mut self, game: &Game) -> Vec<MoveType> {
        let mut moves = vec![Skip; N];
        for crane_id in 0..N {
            let cell = game.board.get_crane_cell(crane_id);
            if cell.is_none() {
                continue;
            }
            let cell = cell.unwrap();
            let coord = cell.coord;

            if coord.is_left_edge() && !cell.crane_grab.unwrap() {
                moves[crane_id] = Grab;
            }

            if !coord.is_right_edge() && cell.crane_grab.unwrap() {
                moves[crane_id] = Move(Right);
            }

            if coord.is_right_edge() && cell.crane_grab.unwrap() {
                moves[crane_id] = UnGrab;
            }

            if !coord.is_left_edge() && !cell.crane_grab.unwrap() {
                moves[crane_id] = Move(Left);
            }
        }

        moves
    }
}

#[derive(Debug)]
struct Task {
    container_id: usize,
    dest: Coord,
}

use std::collections::VecDeque;

struct Strategy2 {
    tasks: Option<VecDeque<Task>>,
    current_task: Option<Task>,
}

impl Strategy for Strategy2 {
    fn next_moves(&mut self, game: &Game) -> Vec<MoveType> {
        if self.tasks.is_none() {
            let mut tasks = VecDeque::new();

            for row in 0..N {
                for &container_id in &game.carry_in.aaa[row] {
                    let task = Task {
                        container_id,
                        dest: Coord(container_id / N, N - 1),
                    };
                    tasks.push_back(task);
                }
            }

            self.tasks = Some(tasks);
        }

        if self.current_task.is_none() {
            self.current_task = self.tasks.as_mut().unwrap().pop_front();
        }

        // println!("{:?} {:?}", self.tasks, self.current_task);

        let mut moves = vec![Skip; N];
        for crane_id in 0..N {
            let cell = game.board.get_crane_cell(crane_id);
            if cell.is_none() {
                continue;
            }
            let cell = cell.unwrap();
            let coord = cell.coord;
            let grab = cell.crane_grab.unwrap();

            if crane_id > 0 {
                moves[crane_id] = Bang;
                continue;
            }

            let current_task = self.current_task.as_ref().unwrap();

            if grab {
                let dest = current_task.dest;
                if let Some(dir) = coord.approach(dest, false) {
                    moves[crane_id] = Move(dir);
                } else {
                    moves[crane_id] = UnGrab;
                    self.current_task = None;
                }
            } else {
                let container_id = current_task.container_id;
                let dest = game.board.get_container_cell(container_id).unwrap().coord;
                if let Some(dir) = coord.approach(dest, false) {
                    moves[crane_id] = Move(dir);
                } else {
                    moves[crane_id] = Grab;
                }
            }
        }

        moves
    }
}

trait InRange {
    fn in_range(&self, l: usize, r: usize) -> bool;
}

impl InRange for usize {
    fn in_range(&self, l: usize, r: usize) -> bool {
        l <= *self && *self <= r
    }
}

struct Strategy3 {
    cnt: usize,
}

impl Strategy for Strategy3 {
    fn next_moves(&mut self, game: &Game) -> Vec<MoveType> {
        let mut moves = vec![Skip; N];

        let cnt = self.cnt;
        for crane_id in 0..N {
            if cnt <= 16 {
                if cnt == 0 || cnt == 8 || cnt == 14 {
                    moves[crane_id] = Grab;
                }
                if cnt.in_range(1, 3) || cnt.in_range(9, 10) || cnt == 15 {
                    moves[crane_id] = Move(Right);
                }
                if cnt == 4 || cnt == 11 || cnt == 16 {
                    moves[crane_id] = UnGrab;
                }
                if cnt.in_range(5, 7) || cnt.in_range(12, 13) {
                    moves[crane_id] = Move(Left);
                }
                continue;
            }

            if crane_id > 0 {
                if cnt == 17 {
                    moves[crane_id] = Bang;
                }
                continue;
            }

            let cell = game.board.get_crane_cell(crane_id).unwrap();
            let coord = cell.coord;
            let grab = cell.crane_grab.unwrap();

            if grab {
                let container_id = cell.lifted_container_id.unwrap();
                let dest = Coord(container_id / N, N - 1);
                if let Some(dir) = coord.approach(dest, false) {
                    moves[crane_id] = Move(dir);
                } else {
                    moves[crane_id] = UnGrab;
                }
            } else {
                let mut dest_cell = None;
                for container_id in 0..N * N {
                    let cell = game.board.get_container_cell(container_id);
                    if cell.is_some() {
                        dest_cell = cell;
                        break;
                    }
                }
                let dest = dest_cell.unwrap().coord;
                if let Some(dir) = coord.approach(dest, false) {
                    moves[crane_id] = Move(dir);
                } else {
                    moves[crane_id] = Grab;
                }
            }
        }

        self.cnt += 1;

        moves
    }
}

struct Strategy4 {
    cnt: usize,
    phase: usize,
    tgt_con_id: Option<usize>,
    subcnt: usize,
}

impl Strategy for Strategy4 {
    fn next_moves(&mut self, game: &Game) -> Vec<MoveType> {
        let mut moves = vec![Skip; N];

        let cnt = self.cnt;
        for crane_id in 0..N {
            if cnt <= 16 {
                if cnt == 0 || cnt == 8 || cnt == 14 {
                    moves[crane_id] = Grab;
                }
                if cnt.in_range(1, 3) || cnt.in_range(9, 10) || cnt == 15 {
                    moves[crane_id] = Move(Right);
                }
                if cnt == 4 || cnt == 11 || cnt == 16 {
                    moves[crane_id] = UnGrab;
                }
                if cnt.in_range(5, 7) || cnt.in_range(12, 13) {
                    moves[crane_id] = Move(Left);
                }
                continue;
            }

            if cnt == 17 {
                if crane_id == 0 {
                    moves[crane_id] = Move(Right);
                }
                if crane_id == 1 {
                    moves[crane_id] = Move(Left);
                }
                if crane_id == 3 {
                    moves[crane_id] = Move(Right);
                }
                if crane_id == 4 {
                    moves[crane_id] = Bang;
                }
            }

            if cnt == 18 {
                if crane_id == 0 {
                    moves[crane_id] = Move(Right);
                }
                if crane_id == 1 {
                    moves[crane_id] = Move(Down);
                }
                if crane_id == 3 {
                    moves[crane_id] = Move(Up);
                }
            }
        }

        let mut next_phase = 0;

        if self.cnt == 19 {
            self.phase = 1;
        }

        if self.phase == 1 {
            if self.tgt_con_id.is_none() {
                let crane0_cell = game.board.get_crane_cell(0).unwrap();
                let crane0_coord = crane0_cell.coord;

                let mut cells = vec![];
                for container_id in 0..N * N {
                    let cell = game.board.get_container_cell(container_id);
                    if let Some(cell) = cell {
                        let row = container_id / N;
                        let ord = container_id % N;

                        cells.push((ord - game.carry_out.cnt[row], cell.coord.dist(crane0_coord), container_id));
                    }
                }
                cells.sort();

                self.tgt_con_id = Some(cells[0].2);
            }

            let tgt_con_id = self.tgt_con_id.unwrap();
            let tgt_con_cell = game.board.get_container_cell(tgt_con_id).unwrap();
            let tgt_con_coord = tgt_con_cell.coord;

            // println!("{tgt_con_id:?} {tgt_con_coord:?}");

            let mut all_ok = true;
            for crane_id in 0..=3 {
                let cell = game.board.get_crane_cell(crane_id).unwrap();
                // println!("{crane_id} {tgt_con_coord:?} {:?}", cell.coord);
                if cell.coord.row() < tgt_con_coord.row() {
                    all_ok = false;
                    moves[crane_id] = Move(Down);
                }
                if cell.coord.row() > tgt_con_coord.row() {
                    all_ok = false;
                    moves[crane_id] = Move(Up);
                }
            }

            if all_ok {
                if tgt_con_coord.col() < 3 {
                    self.phase = 2;
                    self.subcnt = 0;
                } else {
                    self.phase = 3;
                    self.subcnt = 0;
                }
            }
        }

        if self.phase == 2 {
            let tgt_con_id = self.tgt_con_id.unwrap();
            let tgt_con_cell = game.board.get_container_cell(tgt_con_id).unwrap();
            let tgt_con_coord = tgt_con_cell.coord;

            moves[0] = Move(Left);

            for crane_id in 1..=3 {
                if crane_id > tgt_con_coord.col() && self.subcnt == 0 {
                    if tgt_con_coord.row() == 0 {
                        moves[crane_id] = Move(Down);
                    } else {
                        moves[crane_id] = Move(Up);
                    }
                }
            }

            if 2 - self.subcnt == tgt_con_coord.col() {
                next_phase = 3;
            }
        }

        if self.phase == 3 {
            for crane_id in 0..=3 {
                let crane_cell = game.board.get_crane_cell(crane_id).unwrap();

                if self.subcnt == 0 {
                    let tgt_con_id = self.tgt_con_id.unwrap();
                    let tgt_con_cell = game.board.get_container_cell(tgt_con_id).unwrap();
                    let tgt_con_coord = tgt_con_cell.coord;

                    if crane_cell.container_id.is_some() && crane_cell.coord.row() == tgt_con_coord.row() {
                        moves[crane_id] = Grab;
                    }
                }
                if self.subcnt == 1 {
                    moves[crane_id] = Move(Right);
                }
                if crane_id >= 1 {
                    if self.subcnt == 2 {
                        if crane_cell.crane_grab.unwrap() {
                            moves[crane_id] = UnGrab;
                        }
                    }
                    if self.subcnt == 3 {
                        moves[crane_id] = Move(Left);
                    }
                } else {
                    if self.subcnt >= 2 {
                        let row = self.tgt_con_id.unwrap() / N;
                        let dir = crane_cell.coord.approach(Coord(row, N - 1), true);

                        if let Some(dir) = dir {
                            moves[0] = Move(dir);
                        } else {
                            if crane_cell.crane_grab.unwrap() {
                                moves[0] = UnGrab;
                            } else {
                                moves[0] = Move(Left);
                                next_phase = 1;
                            }
                        }
                    }
                }
            }
        }

        self.subcnt += 1;

        if next_phase != 0 {
            self.phase = next_phase;
            self.subcnt = 0;

            if next_phase == 1 {
                self.tgt_con_id = None;
            }
        }

        self.cnt += 1;

        // println!("{:?}", moves.clone());

        moves
    }
}

fn simulate<TStrategy: Strategy>(carry_in: CarryIn, strategy: &mut TStrategy) -> Game {
    let mut game = Game::from(carry_in);

    while !game.finished() {
        game.carry_in();
        game.r#move(strategy);
        game.carry_out();

        // eprintln!("{game}");
        // read_line();
    }

    // eprintln!("{:?}", game.score());

    game
}

fn main() {
    let carry_in = CarryIn::read();

    let mut strategy = Strategy4 {
        cnt: 0,
        phase: 0,
        tgt_con_id: None,
        subcnt: 0,
    };
    let game = simulate(carry_in.clone(), &mut strategy);

    game.score();
    game.print_ans();
}
