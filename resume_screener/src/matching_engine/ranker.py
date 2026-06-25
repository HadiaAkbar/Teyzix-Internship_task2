                               

def rank_candidates(candidate_scores: dict) -> list:
    """Ranks candidates based on their scores."""
                                   
    return sorted(candidate_scores.items(), key=lambda item: item[1], reverse=True)
