require 'csv'

# do you eat steak: "i" -> 8
# household income: "m"-> 12

number_who_eat_steak_0_25 = 0
number_who_dont_eat_steak_0_25 = 0

number_who_eat_steak_25_50 = 0
number_who_dont_eat_steak_25_50 = 0

number_who_eat_steak_50_100 = 0
number_who_dont_eat_steak_50_100 = 0

number_who_eat_steak_100_150 = 0
number_who_dont_eat_steak_100_150 = 0

number_who_eat_steak_150 = 0
number_who_dont_eat_steak_150 = 0

CSV.foreach("steak-risk-survey.csv") do |row|
  income = row[12] # look at the row I'm in, get value from column 12
  eat_steak = row[8]

  if income and eat_steak
    if eat_steak == "Yes"
      if income == "$50,000 - $99,999"
        number_who_eat_steak_50_100 = number_who_eat_steak_50_100 + 1
      elsif income == "$0 - $24,999"
        number_who_eat_steak_0_25 = number_who_eat_steak_0_25 + 1
      elsif income == "$25,000 - $49,999"
        number_who_eat_steak_25_50 = number_who_eat_steak_25_50 + 1
      elsif income == "$100,000 - $149,999"
        number_who_eat_steak_100_150 = number_who_eat_steak_100_150 + 1
      elsif income == "$150,000+"
        number_who_eat_steak_150 = number_who_eat_steak_150 + 1
      end
    elsif eat_steak == "No"
      if income == "$50,000 - $99,999"
        number_who_dont_eat_steak_50_100 = number_who_dont_eat_steak_50_100 + 1
      elsif income == "$0 - $24,999"
        number_who_dont_eat_steak_0_25 = number_who_dont_eat_steak_0_25 + 1
      elsif income == "$25,000 - $49,999"
        number_who_dont_eat_steak_25_50 = number_who_dont_eat_steak_25_50 + 1
      elsif income == "$100,000 - $149,999"
        number_who_dont_eat_steak_100_150 = number_who_dont_eat_steak_100_150 + 1
      elsif income == "$150,000+"
        number_who_dont_eat_steak_150 = number_who_dont_eat_steak_150 + 1
      end
    end
  end
end

#total = number_who_eat_steak + number_who_dont_eat_steak
#percentage_who_dont = number_who_dont_eat_steak / total.to_f
#percentage_who_dont = percentage_who_dont * 100
#percentage_who_dont = percentage_who_dont.round(2)
#puts percentage_who_dont.to_s + "% people do not eat steak"


def output_results(label, who_do, who_dont)
  total = who_do  + who_dont
  percent = who_do / total.to_f
  percent = percent * 100
  percent = percent.round(2)
  puts label+ " " + percent.to_s + "% people who eat steak"
end

output_results("0-25",number_who_eat_steak_0_25, number_who_dont_eat_steak_0_25)
output_results("25-50",number_who_eat_steak_25_50, number_who_dont_eat_steak_25_50)
output_results("50-100",number_who_eat_steak_50_100, number_who_dont_eat_steak_50_100)
output_results("100-150",number_who_eat_steak_100_150, number_who_dont_eat_steak_100_150)
output_results("150+",number_who_eat_steak_150, number_who_dont_eat_steak_150)

# results
#0-25 76.0% people do eat steak
#25-50 76.62% people do eat steak
#50-100 81.4% people do eat steak
#100-150 88.0% people do eat steak
#150+ 75.93% people do eat steak

# change to get from column 7 to see cheating results
#0-25 17.65% people who cheated
#25-50 15.58% people who cheated
#50-100 20.93% people who cheated
#100-150 10.53% people who cheated
#150+ 22.22% people who cheated
