async function notifyTeam(event) {
  const message = {
    type: event.type,
    status: event.status,
    repository: event.repository,
    branch: event.branch,
    commit: event.commit,
    timestamp: new Date().toISOString(),
  };

  await sendSlack(message);
  await sendTeams(message);

  return {
    notified: true,
    channels: ["slack", "teams"],
  };
}
