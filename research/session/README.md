# Active research context

`active-context.json` is the reusable working set for adjacent turns. It stores node IDs and short state, never full research notes.

Reuse it when the new request continues the same topic. Re-route from the compact index when the topic changes materially, the cache is stale, or the user's query names a different object. Clear it at the end of a session when asked, or when carrying it forward would bias unrelated work.

Do not treat the session file as empirical evidence or a replacement for graph updates. Durable conclusions belong in graph nodes.
