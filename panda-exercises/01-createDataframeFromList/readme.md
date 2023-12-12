# Create a DataFrame from List
> Crie um DataFrame da lista

Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
> Escreva uma solução para criar um DataFrame a partir de uma lista 2D chamada student_data. Esta lista 2D contém as IDs e idades de alguns alunos.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
> O DataFrame deve ter duas colunas, student_ide age, e estar na mesma ordem que a lista 2D original.

The result format is in the following example.
>O DataFrame deve ter duas colunas, student_ide age, e estar na mesma ordem que a lista 2D original.

 

Example 1:

Input:
`student_data`:
``` python
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
```

`Output`:
```
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
```

**Explanation**:

A DataFrame was created on top of student_data, with two columns named student_id and age.
> Um DataFrame foi criado sobre student_data, com duas colunas denominadas student_ide age.