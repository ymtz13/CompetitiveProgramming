using System;

public class PriorityQueue<T> where T: IComparable
{
        private IComparer<T> _comparer = null;
        private int _type = 0;

        private T[] _heap;
        private int _sz = 0;

        private int _count = 0;

        /// <summary>
        /// Priority Queue with custom comparer
        /// </summary>
        public PriorityQueue(int maxSize, IComparer<T> comparer)
        {
            _heap = new T[maxSize];
            _comparer = comparer;
        }

        /// <summary>
        /// Priority queue
        /// </summary>
        /// <param name="maxSize">max size</param>
        /// <param name="type">0: asc, 1:desc</param>
        public PriorityQueue(int maxSize, int type = 0)
        {
            _heap = new T[maxSize];
            _type = type;
        }

        private int Compare(T x, T y)
        {
            if (_comparer != null) return _comparer.Compare(x, y);
            return _type == 0 ? x.CompareTo(y) : y.CompareTo(x);
        }

        public void Push(T x)
        {
            _count++;

            //node number
            var i = _sz++;

            while (i > 0)
            {
                //parent node number
                var p = (i - 1) / 2;

                if (Compare(_heap[p], x) <= 0) break;

                _heap[i] = _heap[p];
                i = p;
            }

            _heap[i] = x;
        }

        public T Pop()
        {
            _count--;

            T ret = _heap[0];
            T x = _heap[--_sz];

            int i = 0;
            while (i * 2 + 1 < _sz)
            {
                //children
                int a = i * 2 + 1;
                int b = i * 2 + 2;

                if (b < _sz && Compare(_heap[b], _heap[a]) < 0) a = b;

                if (Compare(_heap[a], x) >= 0) break;

                _heap[i] = _heap[a];
                i = a;
            }

            _heap[i] = x;

            return ret;
        }

        public int Count()
        {
            return _count;
        }

        public T Peek()
        {
            return _heap[0];
        }

        public bool Contains(T x)
        {
            for (int i = 0; i < _sz; i++) if (x.Equals(_heap[i])) return true;
            return false;
        }

        public void Clear()
        {
            while (this.Count() > 0) this.Pop();
        }

        public IEnumerator<T> GetEnumerator()
        {
            var ret = new List<T>();

            while (this.Count() > 0)
            {
                ret.Add(this.Pop());
            }

            foreach (var r in ret)
            {
                this.Push(r);
                yield return r;
            }
        }

        public T[] ToArray()
        {
            T[] array = new T[_sz];
            int i = 0;

            foreach (var r in this)
            {
                array[i++] = r;
            }

            return array;
        }
}

class Program
{
    static void Main()
    {
        string buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(buf[0]),
            M = int.Parse(buf[1]),
            S = int.Parse(buf[2]);

        var E = new int[N, N, 2];
        for(int i=0; i<M; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            int U = int.Parse(buf[0]),
                V = int.Parse(buf[1]),
                A = int.Parse(buf[2]),
                B = int.Parse(buf[3]);
            E[U-1, V-1, 0] = A;
            E[U-1, V-1, 1] = B;
        }

        var C = new int[N, 2];
        for(int i=0; i<M; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            int C = int.Parse(buf[0]),
                D = int.Parse(buf[3]);
            E[i, 0] = C;
            E[i, 1] = D;
        }

        int M = 2600;
        var d = new int[N, M];
        for(int i=0; i<N; ++i) for(int j=0; j<M; ++j) d[i,j]=-1;
        d[0,S]=0;
        
        

        

    }

}
