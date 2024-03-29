Variants

- line
- monochrome (solid, but with no fill and with class atrributes that can be defined by user theme)
- solid
- thinline

## The monochrome icon

The monochrome icon's source svg has no color definitions, only the classes are applied. to use this svg file, we need to alter the svg on the go.

Currently (Dec 2022) there are 5 classes found. and the script used by unicons team can be found [here (/scripts/monochrome/replaceFill.js)](https://github.com/Iconscout/unicons/blob/master/scripts/monochrome/replaceFill.js)

- `uim-primary`
- `uim-secondary`
- `uim-tertiary`
- `uim-quaternary`
- `uim-quinary`

(from /scripts/monochrome/replaceFill.js)

```js
const COLOR_CLASS = {
  'fill="#6563ff"': 'class="uim-primary"',
  'fill="#8c8aff"': 'class="uim-secondary"',
  'fill="#b2b1ff"': 'class="uim-tertiary"',
  'fill="#d8d8ff"': 'class="uim-quaternary"',
  'fill="#ffffff"': 'class="uim-quinary"',
  'fill="#fff"': 'class="uim-quinary"',
};
```

Example of monochrome icon svg

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="6" class="uim-tertiary" />
  <path
    class="uim-primary"
    d="M12,2A10,10,0,1,0,22,12,10.01146,10.01146,0,0,0,12,2Zm0,16a6,6,0,1,1,6-6A6.00687,6.00687,0,0,1,12,18Z"
  />
</svg>
```

## Sanitization

1. There is redundant attribute `data-name` in the svg files. This is generated by their design tools, and can be safely removed.

## Meta data format

The official metadata from unicons are constructed like below.

```json
{
  "id": 1237533,
  "name": "0-plus",
  "svg": "svg/line/0-plus.svg",
  "category": "User Interface",
  "style": "Line",
  "tags": [
    "age-restriction",
    "age-limit",
    "age",
    "restriction",
    "zero-plus",
    "0-plus"
  ],
  "code": 60406,
  "unicode": "ebf6",
  "pro": false
}
```
