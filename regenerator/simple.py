import threading
import queue

def duplicate(generator):
    q1 = queue.Queue()
    q2 = queue.Queue()

    class End:
        def __init__(self):
            pass
    end = End()

    def queue_to_generator(q):
        while True:
            item = q.get()
            if isinstance(item, End):
                break
            yield item

    def producer():
        for item in generator:
            q1.put(item)
            q2.put(item)
        q1.put(end)
        q2.put(end)

    threading.Thread(target=producer, daemon=True).start()
    return queue_to_generator(q1), queue_to_generator(q2)

g1, g2 = duplicate(range(5))

print("from g1:")
for x in g1:
    print(x)

print("from g2:")
for x in g2:
    print(x)

