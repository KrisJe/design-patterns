# producer
class MyJob(object):
    def on_progress(self, pct):
        """Called when progress is made. pct is the percent complete.
        By default this does nothing. The user may override this method
        or even just assign to it."""
        pass

    def run(self):
        n = 10
        for i in range(n):
            self.on_progress(100.0 * i / n)
        self.on_progress(100.0)

# consumer
import sys

job = MyJob()
job.on_progress = lambda pct: sys.stdout.write("%.1f%% done\n" % pct)
job.run()