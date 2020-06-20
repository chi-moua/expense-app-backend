#echo expense-app-backend

# Database Schemas

### Expense
This table holds all the expenses.
| Attribute | Type |
| --------- | ----- |
| id | Integer |
| date | Datetime |
| amount | Float |
| business | String |
| type | String |
| description | String |


### Travel Expense
This schema holds the foreign keys to the travel
related expenses and trips.
| Attribute | Type |
| --------- | ----- |
| id | Integer |
| expense_id | Integer, ForeignKey(Expense)|
| trip_id | Integer, ForeignKey(Trip) |


### Trips
This table holds information related to a specific
trip.
| Attribute | Type |
| --------- | ----- |
| id | Integer |
| name | String |
| start_date | Datetime |
| end_date | Datetime | 
| description | String |