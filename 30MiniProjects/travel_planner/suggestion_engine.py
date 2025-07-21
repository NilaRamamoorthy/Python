def suggest_destination(preferred_destinations, all_destinations):
    suggestions = set(all_destinations) - set(preferred_destinations)
    return suggestions if suggestions else {"No new suggestions available"}
