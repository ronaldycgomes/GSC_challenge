# Giant Steps Capital internship challenge - Code explanation 

<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<div id="badges" align='center'>
  <a href="https://www.linkedin.com/in/ronaldy-gomes-a9581760/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>


Hello, my name is Ronaldy, and I will explain my challenge solution in this readme step by step. 

First, I would like to thank you all for the opportunity to show my skills in this challenge. Just here, I had the opportunity to learn a thousand of methods and funcions in this technology. Imagine if I could work with you!

# Code Explanation:

![image](https://user-images.githubusercontent.com/64624525/173992212-e61032e1-8c9c-4982-bd9a-fc72800cd462.png)

- In this piece of code I am doing all the libraries imports that I will use to build my solution.

![image](https://user-images.githubusercontent.com/64624525/173992497-5d552386-a7e1-44b7-8d09-d7a128a5880c.png)

- Here, I am requesting(with prints) and storing(in variables) all the user inputs that the challenge requires.

![image](https://user-images.githubusercontent.com/64624525/173992708-ca7a20d2-9496-419b-8666-5e87628ea2a7.png)

- Here, I started to develop the 'day' case solution. First, I stored the BCB API URL, and build a logic(using the string .REPLACE method) to insert the 'start date' and 'end date' inside the URL, creating a new one called 'final_url'. After this, I create a DataFrame(using pandas library) and store all the API response in this dataframe(using the read_json method).
- Obs: I decided to start with the 'day' case because all my solution is based on this case. I mean, the 'month' and 'year' cases will uses the same logic, but with particular changes.

![image](https://user-images.githubusercontent.com/64624525/174000023-2036cc04-df50-4e12-944d-e725ba54bd8a.png)

- Here, I decided to do a 'start date' validation. in other words, when we have a 'start date' that is different from the first dataframe date, we delete the first row in the dataframe. Why? When you request a 'start date' in the BCB API, and on that day there is not SELIC rate, the API returns the day before(that contains SELIC rate) as first day in the JSON. Thats why we delete the first row. In this way, the first day in the dataframe will always be the first date(after 'start date') that has SELIC rate.
- About the code, first I convert the 'start date' into datetime type, in order to compare with other dates. After this, I catch the first date on the API response(in the dataframe), store in a variable and also convert to a datetime type. With the two dates with the same type, I compare, and if they are different, I apply the logic in explained before. 
- Obs: It is important to note that in the case I delete the first row, the indexation is different. That why I add 1 unity to the variable 'total_days' that stores the lenght of the dataframe. In this way, we will not fall in an 'index out of range' error.

![image](https://user-images.githubusercontent.com/64624525/174000137-e4294d65-d2b1-48d2-8d13-b07d92fd88db.png)

- Here, I develop the logic that builds and calculates the 'capital' column. I decided to store all the values in a list, and after the calculations, I incorporate this list as a column in the dataframe. It is important to note that I also store the rates(from the BCB API) in another list to make the calculations easier(because of the indexes). The logic to calculates the accrued rates is basically uses the neutral element of multiplication(1) to multiply the rate(i) * rate(i+1) through the iterations. The formula is:

![image](https://user-images.githubusercontent.com/64624525/174001448-0a6952a8-968f-4b15-bf52-66dd01691974.png)

- About the code: First I use a for loop(the first one) to go through the dataframe. Inside this loop, I use an IF statement in case we are talking about the first row(in this case, the acrrued rate == 0, and the capital = 'capital' variable). In the ELSE statement I calculate the acrrued rate and store in list. It is important to note that I need to cast the rate to FLOAT type to do all the calculations. In the second for loop I calculte the CAPITAL value using the accrued rates, just multipling them, and store in the capital_column list.

![image](https://user-images.githubusercontent.com/64624525/174000844-72d2b236-be72-43c5-957a-d06b77ad1bee.png)

- Here, in the first part, I just add the capital_column list as a column in the dataframe. After this, I create the 'amount earned' list, that will be a column too. The logic to calcultes the amount earned is simple. You just need to subtract the 'capital' value(we just calculated in the last print) from the initial 'capital'(defined in the beggining of the code). To calculates all the lines, we just use a for loop to(reminder to the first row case here too).

![image](https://user-images.githubusercontent.com/64624525/173999796-768bd9bd-6157-4b2f-81ff-90f2f8802cb4.png)

- Here, in the first part I just add the 'amount earned' list as a dataframe column, and in the second part, I convert all the 'date' column in to DATETIME values.

![image](https://user-images.githubusercontent.com/64624525/174083149-515d2f6b-4703-4ef3-86cd-163f28031eed.png)

- Here, is the logic for the user's choice for frequency. If he chooses 'day', the code just output the day dataframe that we just had created. Here, note that I deleted the rate value column in the command 'del df['valor']'. And if the user chooses the frequency 'month' or 'year', the code will execute another code block, that I will explain in the next steps.

- ![image](https://user-images.githubusercontent.com/64624525/174092149-c588d266-5887-4e27-9d19-19f4b072592d.png)

- In this piece of code I start to develop the 'month' case logic. In resume, I will use the 'day' case solution to generate the main dataframe. Based on this dataframe, I will develop the logic to get the 'monthly' dataframe. The general idea is to store(in lists) all the lines that are the last day in the month that has SELIC rate in that day, with their respective accrued capital and accrued rates in that line. 
- About the code: First I create all the lists that I will use to store these lines, and after all the logic, they will build the new 'monthly dataframe', and that will be the 'monthly case' output. After this, we can see the firts IF statement that build the logic in the case I delete the first row. Inside this first IF statement, we have the logic for the last line case. In short, if we are in the last line in the dataframe, we can not use the usual iteration. Like you see, in line 93 and 94, there is a logic to compare the actual month to the next month(the month of the next day), and if we are in the last dataframe line, we can use df[data[i+1]] (that would cause an index error). So, because of that, we just fill the last line with the end date, its capital and amount earned values from the main dataframe.

![image](https://user-images.githubusercontent.com/64624525/174106430-d84adbc0-e974-40c4-8fd7-0af39d6090b1.png)

- In this piece of code, first I create a new dataframe, and that will be the output for the 'month' case. After this, I incorporate the lists with all the information we got with the logic I explained before, as columns in this new dataframe. Then, I just display the output.

![image](https://user-images.githubusercontent.com/64624525/174108450-9c209474-3921-4608-8445-f261455fa27c.png)

- Here, in this ELSE statement, I use the same logic, but with different indexation(in the case I don't delete the first row).
- Obs: In the lines 91, 98, 110 and 117 I had to use ILOC method because I can't refer 'amount earned' as column name in the normal referenciation I used in the other cases(line 108 and 109, for example). Why? Because of the blank space in the string.

![image](https://user-images.githubusercontent.com/64624525/174111901-f55ea9a1-d5f5-4c00-a1fc-a2306d1db964.png)

- Here, I basically used the same logic used in the 'month' case, but changed the method that catch the month from a specific day, to a method that catch the year of a specific day. After that, I did the same comparation in proceed with the same logic. In the end, as the last case, I create a new dataframe to use as output.
 
 ![image](https://user-images.githubusercontent.com/64624525/174115928-ba46a15a-64c8-41f9-acba-86e3a2146ebb.png)

- As I explained in the last step, I used the same logic that I apply in the 'month' case, but just changing the .MONTH method to .YEAR method.


- In general lines, the code works for all scenarios I tested: <br/>
-Start date and End date as weekdays; <br/>
-Start date as weekday and End date as weekend; <br/>
-Start date as weekend and End date as weekday; <br/>
-Start date and End date as weekend.

 



