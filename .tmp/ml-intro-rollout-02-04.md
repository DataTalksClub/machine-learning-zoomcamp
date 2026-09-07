# ML Zoomcamp intro screenshot rollout

This report records every screenshot in the three assigned lessons. Originals
remain in place; accepted replacements are sibling assets.

## 02-ml-vs-rules

### 02-ml-vs-rules-01-spam-examples.jpg

- Disposition: `imagegen`; the two example email cards directly support the
  spam-detection setup.
- Invariant: title `Spam`; two overlapping cards; `Get 50% off now` from
  `promotions@online.com`; `URGENT: tax review` from `tax@online.com`; the
  tax-review warning, URL, and `Tax office.` remain readable.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-01-spam-examples-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; exact headers, URL,
  warning, and two-card relationship checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-03-more-spam.jpg

- Disposition: `imagegen`; the prize/deposit email is the concrete example
  that motivates adding a new spam rule.
- Invariant: title `More`; one bordered email; `Waiting for your reply`,
  `prince1@test.com`, the 1.000.000-dollar claim, `$10`,
  `prince@test.com`, transfer message, and `Congratulations again!` remain
  readable.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-03-more-spam-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; exact amount, dollar
  fee, email addresses, and single-card relationship checked; face, webcam,
  browser/Zoom chrome, cursor, watermark, toolbar, and recording overlays
  absent.

### 02-ml-vs-rules-04-features.jpg

- Disposition: `imagegen`; the feature list makes the transition from rules
  to numerical ML inputs concrete.
- Invariant: title `Features`; six bullets in source order, including both
  sender addresses, `test.com`, and `deposit`; the `Rules` cue remains on the
  right.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-04-features-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all six labels and
  the `Rules` cue checked verbatim; face, webcam, browser/Zoom chrome,
  cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-05-encode-email.jpg

- Disposition: `imagegen`; the email-to-vector mapping is the lesson's key
  feature-encoding example.
- Invariant: email content and `SPAM` badge; `Sender
  promotions@online.com? False`; exact vector `[1, 1, 0, 0, 1, 1]`; arrow
  from the sender feature to the vector.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-05-encode-email-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; email labels, vector
  values/order, badge, and mapping checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-02-rules.jpg

- Disposition: `imagegen`; the three hard-coded rules are the lesson's
  contrast with learned rules.
- Invariant: title `Rules`; exact three bullet rules and their order, including
  `promotions@online.com`, `tax review`, `online.com`, `spam`, and
  `good email`.
- Crop: `480x280+20+30` from the 598x360 source.
- Output: `02-ml-vs-rules-02-rules-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all three bullets and
  order checked verbatim; face, webcam, browser/Zoom chrome, cursor,
  watermark, toolbar, and recording overlays absent.
