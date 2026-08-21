function validateCoverage(coverage) {
  const minimum = {
    lines: 80,
    statements: 80,
    functions: 75,
    branches: 70,
  };

  return (
    coverage.lines >= minimum.lines &&
    coverage.statements >= minimum.statements &&
    coverage.functions >= minimum.functions &&
    coverage.branches >= minimum.branches
  );
}
