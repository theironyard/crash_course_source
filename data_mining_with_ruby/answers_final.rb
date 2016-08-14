require 'csv'

# do you eat steak: "i" -> 8
# household income: "m"-> 12

yes_0_25 = 0
no_0_25 = 0

yes_25_50 = 0
no_25_50 = 0

yes_50_100 = 0
no_50_100 = 0

yes_100_150 = 0
no_100_150 = 0

yes_150 = 0
no_150 = 0

CSV.foreach("steak-risk-survey.csv") do |row|
  income = row[12] # look at the row I'm in, get value from column 12
  eat_steak = row[8]

  if income and eat_steak
    if eat_steak == "Yes"
      if income == "$50,000 - $99,999"
        yes_50_100 = yes_50_100 + 1

      elsif income == "$0 - $24,999"
        yes_0_25 = yes_0_25 + 1

      elsif income == "$25,000 - $49,999"
        yes_25_50 = yes_25_50 + 1

      elsif income == "$100,000 - $149,999"
        yes_100_150 = yes_100_150 + 1

      elsif income == "$150,000+"
        yes_150 = yes_150 + 1
      end

    elsif eat_steak == "No"
      if income == "$50,000 - $99,999"
        no_50_100 = no_50_100 + 1

      elsif income == "$0 - $24,999"
        no_0_25 = no_0_25 + 1

      elsif income == "$25,000 - $49,999"
        no_25_50 = no_25_50 + 1

      elsif income == "$100,000 - $149,999"
        no_100_150 = no_100_150 + 1

      elsif income == "$150,000+"
        no_150 = no_150 + 1

      end
    end
  end
end

#total = yes + no
#percentage_who_dont = no / total.to_f
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

output_results("0-25",yes_0_25, no_0_25)
output_results("25-50",yes_25_50, no_25_50)
output_results("50-100",yes_50_100, no_50_100)
output_results("100-150",yes_100_150, no_100_150)
output_results("150+",yes_150, no_150)

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
