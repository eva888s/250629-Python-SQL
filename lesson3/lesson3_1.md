## 建立資料表語法
```
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```
## 建立一個student的表格
```sql
CTREATE TABLE IF NOT EXISTS STUDENT(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    MAJOR VACHAR(20) UNIQUE
);
```


## 刪除資料表

```sql
DROP TABLE IF EXISTS STUDENT;
```

## 新增1筆資料

```sql
INSERT INTO STUDENT (NAME, MAJOR)
VALUES ('呂育君','歷史');
```

## 新增多筆資料
```sql
INSERT INTO STUDENT (NAME, MAJOR)
VALUES ('小柱','生物'),('信忠','英語');
```