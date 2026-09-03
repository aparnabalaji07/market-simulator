# To-Do List

## Phase 1

- [x] **TASK:** buy/sell/total-worth logic
  - **WHY:** understand how basic market functions work. backbone of the whole project
  - **DONE WHEN:** buying 10 @ $50 leaves worth unchanged at $1000, and after rise to $55 worth reads $1050. the numbers move correctly by hand.
  - **DAY:** day 1

- [x] **TASK:** walk-forward loop with look-ahead guard
  - **WHY:** understanding how to properly analyze past stock data without letting future days affect a prediction. if we are on day 4 and the program can access or see day 50, it will use that number unknowingly as a prediction. this makes the prediction reliable, not from data already seen.
  - **DONE WHEN:** each day the printed average only reflects earlier days. day 0 shows N/A.
  - **DAY:** day 1

- [x] **TASK:** momentum and mean-reversion strategies
  - **WHY:** most basic trading strategies. implement this along with the buy/sell/total worth code to look at how different trading strategies output different final portfolio values
  - **DONE WHEN:** momentum outputs final worth 1060 and mean reversion 1030 on the test price and each trade in log matches the rule.
  - **DAY:** day 1

- [ ] **TASK:** wrap state in a portfolio class, guard inside sell
  - **WHY:** clean up the code written. put groups and actions that are related together. this will help the code stay organized as i grow the project. a guard is needed inside to sell to ensure the user actually has shares to sell before they try to sell something.
  - **DONE WHEN:** both strategies still output 1060/1030 after all cash and share logic moves in the class. attempts to sell more shares than owned is blocked by the guard.
  - **DAY:** day 2

- [ ] **TASK:** track realized vs unrealized profit and loss
  - **WHY:** sometimes it may seem like the value of a portfolio is higher than it is. realized profit are stocks converted into actual money. unrealized can change at anytime as the stock has not been sold yet. if unrealized profit is accidentally categorized as realized profit, there is a chance that the stock price will decrease before the user can sell it and have lesser liquid cash when they do eventually sell. it is misleading if profit is not separated as realized and unrealized.
  - **DONE WHEN:** portfolio reports realized and unrealized separately and i can verify this with my own calculation. holding 10 shares for $5 each shows $50 unrealized, $0 realized, after selling, $0 unrealized, $50 realized.
  - **DAY:** day 2

- [ ] **TASK:** add performance metrics (return, drawdown, Sharpe)
  - **WHY:** to see statistics of how a run performed. total return is how much the money grew overall (should be a percentage not $ because $ can look very different based on starting values ex. starting with $10 vs $100) whereas percentage will stay the same regardless of starting and ending prices. drawdown is how far the money fell from its highest point. shows how stressful watching the stock could have been for the user (emotions are important in trading!). the sharpe ration is the number that is used to see if the gains recieved that were worth the risk taken to get them. to calculate sharpe ratio find different equations online and pick the best fit. this day will require extra research. do more research on sharpe ration and common mistakes when implementing it.
  - **DONE WHEN:** finished run prints total return as %, max drawdown as %, and sharpe number i calculate.
  - **DAY:** day 3

- [ ] **TASK:** add transaction costs
  - **WHY:** everytime you buy or sell in the real stock market, there is a small fee. if the test does not have that fee, then results may look better than they would in real life. (should i research the different fees and allow user to choose which portfolio they have to account for fees? -- something to do during website development and ux)
  - **DONE WHEN:** print final worth with and without fees; with fees should be lower than without. difference should be number of trades x fee per trade. this confirms the fee was applied.
  - **DAY:** day 3

- [ ] **TASK:** load real prices from a csv
  - **WHY:** allows for historical data to be tested instead of random numbers in an array. tests will run using actual historical data instead of fake data.
  - **DONE WHEN:** same strategy runs on price file. no changes except data source. output should have an accurate final worth over the historical data.
  - **DAY:** day 4

- [ ] **TASK:** record the equity curve
  - **WHY:** to see the overall gain/loss of a test. write down the account value at the end of the day and once the test is done, take the list of account values and create a graph to show the loss and gain of the money over time. tldr: gather data points of account value EVERY DAY then plot it.
  - **DONE WHEN:** after run there is a list showing the worth of portfolio after each day. a line graph should also be produced at the end showing the account rising and falling over time.
  - **DAY:** day 5
