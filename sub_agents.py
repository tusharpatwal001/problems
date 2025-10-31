from prompts import SUB_PRESENTATION_MAKER_PROMPT
from tools import (
    generate_presentation,
)

presentation_maker_sub_agent = {
    "name": "presentation-maker",
    "description": "Used to create presentation of the final output. Give this agent some information about the presentation and number of slides.",
    "system_prompt": SUB_PRESENTATION_MAKER_PROMPT,
    "tools": [
        generate_presentation,
    ],
}
