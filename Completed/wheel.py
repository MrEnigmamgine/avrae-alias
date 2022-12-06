!tembed <drac2>

cal= load_json(get_gvar("cbe88a78-fc52-43d3-a669-5b8ee38dea7c"))

year_len = cal.length

year = int(get_uvar('curyear'))
## TODO: Handle incrementing year when year wraps over

#get day of year
date = int(get_uvar('curdate')) % year_len

# Increment for convenience
# set_uvar('curdate', date+1)

#get name of weekday
weekday = cal.weekdays[(date-1)%len(cal.weekdays)]

# get day of month and month
day = date
for i, month in enumerate(cal.months):
    if day > month.length:
        day -= month.length
    else:
        cur_month = month.name
        cur_month_i = i+1
        break

# get language suffix
def date_suffix(day):
    z=int(str(day)[-1:])
    return 'th' if 14>int(day)>10 \
        else 'st' if z == 1 \
        else 'nd' if z == 2 \
        else 'rd' if z == 3 \
        else 'th'
suffix = date_suffix(day)

#TODO: Check for holidays

#Get the season
cur_season = ""
for season in cal.seasons:
    if season.start < date < season.end:
        cur_season = season.name
        break


out = [cur_month_i, cur_month, day, suffix, weekday, cur_season]

desc_text = f"{weekday}day, the {day}{suffix} of {cur_month}"

#TODO: 🌌

</drac2>
-title "{{cal.name}}"
-desc "{{desc_text}}"
-f "Year {{year}}|{{cur_season}}|inline"
-footer "!wheel [{{date}}/{{year_len}}]"
