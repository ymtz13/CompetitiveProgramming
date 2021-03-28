using System;
using System.Collections.Generic;

class Node<T>
{
    public Node(int key, T value) {
        Key = key;
        Value = value;
    }

    public int Key { get; }
    public T Value { get; }

    public override string ToString() {
        return $"[{Key}: {Value.ToString()}]";
    }
}

class HeapQueue<T>
{
    private List<Node<T>> heap;
    private List<int> pos;
    public int Count { private set; get; } = 0;

    Comparison<T> comparison;
    
    public HeapQueue(Comparison<T> comparison) {
        heap = new List<Node<T>>{　null　};
        pos = new List<int>();
        this.comparison = comparison;
    }

    public int Push(T value) {
        int index = ++Count;
        int key = pos.Count;
        pos.Add(index);
        var node = new Node<T>(key, value);
        
        if(index < heap.Count) {
            heap[index] = node;
        } else {
            heap.Add(node);
        }

        BubbleUp(index);

        return key;
    }

    public Node<T> Pop(int key = -1) {
        var index = key == -1 ? 1 : pos[key];
        var node = heap[index];

        var index_last = Count;
        if (index < index_last) {
            var node_last = heap[index_last];
            heap[index] = node_last;
            pos[node_last.Key] = index;

            BubbleUp(index);
            BubbleDown(index);     
        }

        --Count;
        return node;
    }

    public void Update(int key, T value) {
        var index = pos[key];
        heap[index] = new Node<T>(key, value);
        BubbleUp(index);
        BubbleDown(index);
    }

    public Node<T> Peek() {
        return heap[1];
    }

    public override string ToString() {
        var lines = new List<string>();
        lines.Add($"Count: {Count}");
        for(int l=0; l<4; ++l) {
            var nodes = new List<string>();
            for(int index=(1<<l); index<(2<<l); ++index) {
                if(index>Count) break;
                nodes.Add($"{heap[index], -10} ");
            }
            if(nodes.Count>0) lines.Add($"({l}): " + string.Join("", nodes));
        }
        return string.Join(Environment.NewLine, lines);
    }

    private void BubbleUp(int index) {
        if (index==1) return;

        var index_parent = index >> 1;

        var node        = heap[index       ];
        var node_parent = heap[index_parent];
            
        if (comparison(node.Value, node_parent.Value) < 0) {
            heap[index       ] = node_parent;
            heap[index_parent] = node       ;
            pos[node       .Key] = index_parent;
            pos[node_parent.Key] = index       ;

            BubbleUp(index_parent);
        }
    }

    private void BubbleDown(int index) {
        var index_lchild = index << 1;
        var index_rchild = index_lchild + 1;

        if (index_lchild > Count) return;

        int index_child = (index_rchild > Count || comparison(heap[index_lchild].Value, heap[index_rchild].Value) <= 0)
            ? index_lchild
            : index_rchild;
        
        var node       = heap[index      ];
        var node_child = heap[index_child];

        if (comparison(node.Value, node_child.Value) > 0) {
            heap[index      ] = node_child;
            heap[index_child] = node       ;
            pos[node      .Key] = index_child;
            pos[node_child.Key] = index       ;

            BubbleDown(index_child);
        }
    }
}

class Program
{
    public static void Main()
    {
        var h = new HeapQueue<int>(delegate(int x, int y){ return x-y; } );
        Console.WriteLine(h.Count);
        Console.WriteLine(h.Push(30));
        Console.WriteLine(h.Push(10));
        Console.WriteLine(h.Push(-90));
        Console.WriteLine(h.Push(+20));
        Console.WriteLine(h.Push(-50));
        Console.WriteLine(h.Push(-40));
        Console.WriteLine(h.Push(+70));
        Console.WriteLine(h);
        Console.WriteLine(h.Pop());
        Console.WriteLine(h);
    }
}
