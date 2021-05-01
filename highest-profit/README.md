# Highest-Profit Challenge

I have used pandas library to process the data fast.

# Instructions to run the code

Both the challenges contain the run.bat file, which can be used to install the required libraries and run the solution code.

I have run my solution using python. If it doesn't work, please feel free to change it to pip3 or python3 in the run.bat file depending on the version of the python installed on the testing machine.

# Input

The code requires a data input which is 'data.csv' in the working directory.

# Output

When you run the run.bat file, it will install the Pandas library and will run my solution file and performs the below actions. 

1.  Loaded all the data from data.csv into the data frame.
2.  Found the number of total rows to be 25500.
3.  Removes the rows with invalid values. After filtering, the number of rows are 25131
4.  Created a JSON file named 'data2.json'
5.  Prints the top 20 rows with the highest profit.

# My Output
```
Answer 1 : Size before filtering :  25500
Answer 2 : Size after filtering :  25131
Converted filtered CSV data to JSON and saved in data2.json
Top 20 rows with highest profit:
       Year  Rank                 Company  Revenue (in millions)    Profit (in millions)
25001  2005     2             Exxon Mobil               270772.0                25330.0
22001  1999     2              Ford Motor               144416.0                22071.0
24501  2004     2             Exxon Mobil               213199.0                21510.0
24507  2004     8               Citigroup                94713.0                17853.0
23000  2001     1             Exxon Mobil               210392.0                17720.0
25007  2005     8               Citigroup               108276.0                17046.0
25004  2005     5        General Electric               152363.0                16593.0
23501  2002     2             Exxon Mobil               191581.0                15320.0
24005  2003     6               Citigroup               100789.0                15276.0
24504  2004     5        General Electric               134187.0                15002.0
25017  2005    18   Bank of America Corp.                63324.0                14143.0
23506  2002     7               Citigroup               112022.0                14126.0
24004  2003     5        General Electric               131698.0                14118.0
23505  2002     6        General Electric               125913.0                13684.0
23005  2001     6               Citigroup               111826.0                13519.0
25005  2005     6           ChevronTexaco               147967.0                13328.0
23004  2001     5        General Electric               129853.0                12735.0
23009  2001    10  Verizon Communications                64707.0                11797.0
24002  2003     3             Exxon Mobil               182466.0                11460.0
25023  2005    24                  Pfizer                52921.0                11361.0
```