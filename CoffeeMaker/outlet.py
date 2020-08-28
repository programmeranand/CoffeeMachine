from threading import Thread


class Outlet(Thread):
    """
    Class to represent each outlet's operation
    Here we are simulating each outlet's operation using worker threads
    Worker threads obtain orders from the queue and prepares the beverage
    """
    def __init__(self, queue, function):
        Thread.__init__(self)
        self.queue = queue
        self.function = function

    def run(self):
        while True:
            # Get the work from the queue and expand the arguments
            beverage, ingredients = self.queue.get()
            try:
                self.function(beverage, ingredients)
            finally:
                # Indicate this thread has finished preparing beverage
                self.queue.task_done()
