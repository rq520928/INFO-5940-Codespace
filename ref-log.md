
# ref-log.md

Reflection on Multi-Agent Travel Planner Implementation

Implementing the multi-agent workflow for this travel planner showed how useful it is to incorporate multi agent systems. By separating the creative planning phase from the critical validation phase, I created a system that mirrors how human teams naturally divide complex tasks. The Planner Agent could focus entirely on generating comprehensive, imaginative itineraries without worrying about real time constraints, while the Reviewer Agent brought grounded fact checking through internet searches. This division of labor proved far more effective than attempting to build a single agent that both plans and validates simultaneously, which I initially considered but quickly realized would create conflicting objectives within a single prompt.

The primary challenge I encountered was calibrating the level of detail each agent should provide. My first iteration of the Planner instructions generated overly generic itineraries that lacked specific venue names and concrete logistics, making it nearly impossible for the Reviewer to validate anything meaningful. I addressed this by explicitly requiring the Planner to include named locations, estimated times, and cost breakdowns. Similarly, the Reviewer initially produced vague feedback like "check opening hours" without actually performing searches. I restructured those instructions to mandate internet tool usage for every major activity and to format findings as a Delta List with specific problems and concrete fixes.

The most creative aspect of my design was framing the Reviewer as a constructive collaborator rather than a harsh critic. By instructing it to acknowledge what works well before suggesting improvements, the final output feels more balanced and actionable. I also emphasized solution oriented language, which ensures users receive practical guidance rather than just a list of problems. This approach reflects my understanding that effective validation should improve plans rather than simply tear them down.

External Tools and Assistance

I used Chat GPT to help double check my grammar for the ref log and also to provide a rough idea of the instructions for the agents.