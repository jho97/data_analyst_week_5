import luigi
from luigi import Task, LocalTarget
from luigi.contrib import sqla
from sqlalchemy import String, Float


class DownloadFranceSales(Task):
    def output(self):
        return LocalTarget('france.csv')

    def run(self):
        with self.output().open('w') as f:
            print('May,100', file=f)
            print('June,200', file=f)


class DownloadGermanySales(Task):
    def output(self):
        return LocalTarget('germany.csv')

    def run(self):
        with self.output().open('w') as f:
            print('May,180', file=f)
            print('June,150', file=f)


class CreateDatabase(sqla.CopyToTable):
    def requires(self):
        return [DownloadFranceSales(),
                DownloadGermanySales()]


if __name__ == '__main__':
    luigi.run(['CreateDatabase', '--local-scheduler'])
