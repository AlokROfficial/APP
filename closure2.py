def cum_avg():
    data=[]
    def avg(value):
        data.append(value)
        return sum(data)/len(data)
    return avg
avg_cum=cum_avg()
print(avg_cum(12))
print(avg_cum(13))
print(avg_cum(14))
