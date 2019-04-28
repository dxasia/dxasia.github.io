#!/usr/bin/python3
from slugify import slugify
import pandas as pd
from pathlib import Path
import fire

def zero_pad_cols(df, columns=['start', 'end']):

    def zero_pad(t):
        return "%04d" % t if isinstance(t, int) else None
    for c in columns:
        df[c] = df[c].map(zero_pad)
    return df

class DXAsia:

    def __init__(self, fn='langstn.xls', output='.'):
        self.fn = fn
        self.df = pd.read_excel(self.fn, dtype=object)
        self.output = Path(output)

    def field(self, column):
        folder = self.output / '_data' / column
        if not folder.exists():
            folder.mkdir(parents=True)
        for x in set(self.df[column]):
            if x == '' or not isinstance(x, str): continue
            df_x = self.df[self.df[column] == x]
            del df_x[column]
            zero_pad_cols(df_x).to_csv(str(folder / (slugify(x) + '.csv')), index=False)

    def init(self, column):
        folder = self.output / column
        if not folder.exists():
            folder.mkdir()
        for x in set(self.df[column]):
            if x == '' or not isinstance(x, str): continue
            xs = slugify(x)
            (folder / (xs + '.md')).write_text(
                "---\n"
                "layout: %s\n"
                "title: %s\n"
                "---\n" % (column, xs)
            )


def main():
    fire.Fire(DXAsia)


if __name__ == "__main__":
    main()
