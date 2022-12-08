// merge json files into one.

// taget files
// - line.json
// - monochrome.json
// - solid.json
// - thinline.json

// each file contains an array of object like this
/*
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
*/

const fs = require("fs");
const path = require("path");
const line = require("../line.json"); //JSON.parse(fs.readFileSync(path.join(__dirname, "./line.json")));
const monochrome = require("../monochrome.json"); //JSON.parse(fs.readFileSync("./monochrome.json"));
const solid = require("../solid.json"); //JSON.parse(fs.readFileSync("./solid.json"));
const thinline = require("../thinline.json"); //JSON.parse(fs.readFileSync("./thinline.json"));

const names = new Set();

// seed all names
[...line, ...monochrome, ...solid, ...thinline].forEach((item) =>
  names.add(item.name)
);

const valueof = (key, ...items) => {
  for (const i of items) {
    if (i) {
      if (i[key]) {
        return i[key];
      }
    }
  }
};

const tagsof = (...items) => {
  const set = new Set();
  for (const i of items) {
    if (i) {
      if (i.tags) {
        i.tags.forEach((tag) => set.add(tag));
      }
    }
  }
  return Array.from(set);
};

// loop through all names
const result = [];

names.forEach((name) => {
  const styles = [];

  const _i_line = line.find((item) => item.name === name);
  const _i_monochrome = monochrome.find((item) => item.name === name);
  const _i_solid = solid.find((item) => item.name === name);
  const _i_thinline = thinline.find((item) => item.name === name);
  const _ii = [_i_line, _i_monochrome, _i_solid, _i_thinline];

  if (_i_line) {
    styles.push("line");
  }
  if (_i_monochrome) {
    styles.push("monochrome");
  }
  if (_i_solid) {
    styles.push("solid");
  }
  if (_i_thinline) {
    styles.push("thinline");
  }

  const item = {
    name,
    category: valueof("category", ..._ii),
    tags: tagsof(..._ii),
    code: {
      line: _i_line ? _i_line.code : null,
      monochrome: _i_monochrome ? _i_monochrome.code : null,
      solid: _i_solid ? _i_solid.code : null,
      thinline: _i_thinline ? _i_thinline.code : null,
    },
    styles,
  };

  result.push(item);
});

// create merged meta.json file
fs.writeFileSync(
  path.join(__dirname, "../meta.json"),
  JSON.stringify(result, null, 2)
);
