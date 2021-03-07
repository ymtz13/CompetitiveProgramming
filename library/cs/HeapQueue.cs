using System;
using System.Collections.Generic;

class Node<T>
{
    public Node(int index, T item) {
        Index = index;
        Item = item;
    }

    public int Index { get; set; }
    public T Item { get; }

    
}

class HeapQueue<T>
{
    private List<Node<T>> heap;
    public int Count { private set; get;} = 0;

    Comparison<T> comparison;
    
    public HeapQueue(Comparison<T> comparison) {
        heap = new List<Node<T>>();
        this.comparison = comparison;
    }

    public Node<T> Push(T item) {
        int index = ++Count;
        var node = new Node<T>(index, item);
        
        if(index < heap.Count) {
            heap[index] = node;
        } else {
            heap.Add(node);
        }

        BubbleUp(index);

        return node;
    }


    private void BubbleUp(int index) {
        if (index==1) return;

        var x = heap[index];
        var p = heap[index/2];
            
        if (comparison(x.Item, p.Item)>0) {
            heap[index] = p;
            p.Index = index;
            heap[index/2] = x;
            x.Index = index/2;

            BubbleUp(index/2);
        }
    }

    private void BubbleDown(int index) {
        if (index*2 <= Count) {
            var x = heap[index];
            var c = heap[index*2];
            
            if (comparison(c.Item, x.Item)>0) {
                heap[index] = c;
                c.Index = index;
                heap[index*2] = x;
                x.Index = index*2;
                
                BubbleDown(index*2);
                return;
            }
        }
        
        if (index*2+1 <= Count) {
            var x = heap[index];
            var c = heap[index*2+1];
            
            if (comparison(c.Item, x.Item)>0) {
                heap[index] = c;
                c.Index = index;
                heap[index*2+1] = x;
                x.Index = index*2+1;

                BubbleDown(index*2+1);
                return;
            }
        }     
    }

}

class Program
{
    public static void Main()
    {
        var h = new HeapQueue<int>(delegate(int x, int y){ return x-y; } );
        Console.WriteLine(h.Count);
    }
}
