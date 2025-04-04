from divine import Heaven


class _Test(Heaven):

    def main(self):
        self.barrier()
        self.listen(2, 3)

Test = _Test()
Test.run()
