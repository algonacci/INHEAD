<div align="center">
  <img src="https://user-images.githubusercontent.com/86970816/196214344-785dd3d5-db69-474a-98bf-860b4671ed6e.png" width="250" height="250">
  <h3 align="center">INHEAD</h3>
  <p align="center">
    Indonesian News Headline Dataset
  </p>
</div>

## Description
Sebuah tools sederhana yang membantu menscrape data judul berita dengan bantuan library PyGoogleNews

## Installation
```bash
# Python version 3.7 or newser
$ git clone https://github.com/algonacci/INHEAD.git
$ pip install -r requirements.txt
```

## Arguments
```
--set        : Dataset type, it can be train/test/val
--query      : A keyword to scrape related news
--topic      : A target/label/class given for each news headline
--quantity   : How many data want to be displayed, max 60
```

## Usage
```
# To scrape data
$ python src/scraping.py --set train --query twitter --topic teknologi

# To merge all scraped data
$ python src/merge.py --set train

# To check the result with Pandas Dataframe
$ python src/check_df.py --set train --quantity 60
```

## TODO
- Menentukan topik-topik besar yang ingin diklasifikasi

Sejauh ini sudah ada topik:

- Pendidikan
- Internasional
- Politik
- Kesehatan
- Pariwisata
- Ekonomi
- Bisnis
- Entertainment
- Teknologi

## Target
- [ ] 45.000 train set
- [ ] 5.000 validation set
- [ ] 5.000 test set
