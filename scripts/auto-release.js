function canRelease(context) {
  return (
    context.ci === "passed" &&
    context.tests === "passed" &&
    context.security === "passed" &&
    context.coverage === "passed"
  );
}

function createRelease(version, changelog) {
  if (!version) {
    throw new Error("Release version is required");
  }

  return {
    version,
    changelog,
    tag: `v${version}`,
  };
}

module.exports = {
  canRelease,
  createRelease,
};
