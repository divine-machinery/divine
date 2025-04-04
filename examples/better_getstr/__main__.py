from divine import Heaven


class _Test(Heaven):

    def main(self):
        self.barrier()
        self.listen()

Test = _Test()
Test.run()
