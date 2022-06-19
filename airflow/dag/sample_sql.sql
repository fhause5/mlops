USE default;

DROP TABLE IF EXISTS event_stats_staging;
CREATE TABLE event_stats_staging
AS SELECT date
        , user_id
        , sum(spend_amt) total_spend_amt
     FROM event
    WHERE date = {{ macros.ds }}
      AND user_id <> {{ params.test_user_id }}
    GROUP BY date, user_id;

   INSERT INTO event_stats (
          date
        , user_id
        , total_spend_amt
   )
   SELECT date
        , user_id
        , total_spend_amt
     FROM event_stats_staging;

DROP TABLE event_stats_staging;