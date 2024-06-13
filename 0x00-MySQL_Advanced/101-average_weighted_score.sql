--  script that creates a stored PROCEDURE ComputeAverageWeightedScoreForUsers,
-- that computes AND store the average weighted score FOR ALL students.
-- 
-- Requirements:
-- 
-- Procedure ComputeAverageWeightedScoreForUsers IS NOT taking any input.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    JOIN (
        SELECT 
            u.id AS user_id, 
            SUM(c.score * p.weight) / SUM(p.weight) AS weight_avg
        FROM 
            users AS u
        JOIN 
            corrections AS c ON u.id = c.user_id
        JOIN 
            projects AS p ON c.project_id = p.id
        GROUP BY 
            u.id
    ) AS weighted_scores
    ON u.id = weighted_scores.user_id
    SET u.average_score = weighted_scores.weight_avg;

END;$$
DELIMITER;
