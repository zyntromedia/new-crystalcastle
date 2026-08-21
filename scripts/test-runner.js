const { execSync } = require("node:child_process");

function runTests() {
  try {
    execSync("npm test -- --runInBand", {
      stdio: "inherit",
    });

    return {
      status: "passed",
      exitCode: 0,
    };
  } catch (error) {
    return {
      status: "failed",
      exitCode: error.status ?? 1,
    };
  }
}

module.exports = {
  runTests,
};
