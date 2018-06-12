# 🌒 Low-Light Photo Enhancement

**Graduation Project — B.Sc. Computer Science (Class of 2018)**  
**Author:** Khaled

Most photos of abandoned places are taken in terrible light: dark corridors, tiny windows, no flash allowed.
This project brightens underexposed photos automatically **without** blowing out the highlights, using
adaptive histogram equalization (CLAHE) in the LAB color space followed by automatic gamma correction.

## How it works

1. Convert the photo from BGR to **LAB**.
2. Apply **CLAHE** to the L (lightness) channel only, so the colors don't shift.
3. Measure the mean brightness and pick a **gamma** value automatically.
4. Merge the channels back and save.

## Usage

```bash
pip install -r requirements.txt
python enhance.py dark_photo.jpg enhanced.jpg
python enhance.py dark_photo.jpg enhanced.jpg --clip 3.0 --grid 8
```

| Option   | Default | What it does                              |
|----------|---------|-------------------------------------------|
| `--clip` | 2.0     | CLAHE clip limit (higher = more contrast) |
| `--grid` | 8       | CLAHE tile grid size                      |

## Notes

Tested on low-light photos I took myself inside old buildings around the city.
