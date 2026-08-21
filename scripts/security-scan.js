const { execSync } = require("node:child_process");

const scanners = [
  "npm audit --audit-level=high",
  "npx eslint .",
];

function runSecurityScan() {
  const results = [];

  for (const command of scanners) {
    try {
      execSync(command, {
        stdio: "inherit",
      });

      results.push({
        command,
        status: "passed",
      });
    } catch (error) {
      results.push({
        command,
        status: "failed",
        exitCode: error.status ?? 1,
      });
    }
  }

  return {
    status: results.every((item) => item.status === "passed")
      ? "passed"
      : "failed",
    results,
  };
}

module.exports = {
  runSecurityScan,
};
