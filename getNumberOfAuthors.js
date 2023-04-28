const fs = require("fs");

// let count = 0;

const data = JSON.parse(fs.readFileSync("universities.json", "utf8"));
// const universities = data.map((uni) => ({ ...uni, authorCount: null }));
// console.log("universities", universities);

// fs.readdirSync("./scholar/").forEach((file, index) => {
//   if (file !== ".gitignore") {
//     const json = JSON.parse(fs.readFileSync("./scholar/" + file, "utf8"));
//     count += json.length;
//     universities.find(
//       (uni) => uni.name.localeCompare(file.split(".")[0]) === 0
//     ).authorCount = json.length;
//     console.log(index, ": ", json.length);
//   }
// });

// fs.writeFileSync("universities2.json", JSON.stringify(universities));

// console.log("total: ", count);

fs.writeFileSync(
  "universitiesWithIds.json",
  JSON.stringify(
    data.filter((uni) => uni.id).map((uni, i) => ({ index: i, ...uni }))
  )
);
