WITH RankData AS (
SELECT name AS Character, className as Class, level, COALESCE((SELECT COUNT(*) FROM Duels WHERE id = winnercharacterid GROUP BY winnercharacterid), 0) AS Wins, COALESCE((SELECT COUNT(*) FROM Duels WHERE id = losercharacterid GROUP BY losercharacterid),0) AS Losses
FROM Characters RIGHT OUTER JOIN Duels ON (id = winnercharacterid OR id = losercharacterid)
)
SELECT (Wins - Losses) as Ranking, Character, Wins, Losses, FORMAT('%s-%s', Wins, Losses) as "W-L"
FROM RankData
ORDER BY Ranking DESC;
