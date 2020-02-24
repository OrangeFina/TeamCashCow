{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stock: AAPL\n",
      "DD/MM/YY: 01/02/19\n",
      "DD/MM/YY: 02/03/19\n",
      "Price change trigger %: 1\n",
      "Volume trigger in millions: 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\weeha\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:36: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "C:\\Users\\weeha\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:37: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "C:\\Users\\weeha\\Anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:844: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self.obj[key] = _infer_fill_value(value)\n",
      "C:\\Users\\weeha\\Anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:964: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self.obj[item] = s\n"
     ]
    }
   ],
   "source": [
    "# function to collect stock query\n",
    "\n",
    "from datetime import datetime\n",
    "import numpy as np\n",
    "import pandas as pd \n",
    "import requests\n",
    "\n",
    "# ask user for input\n",
    "\n",
    "\n",
    "def stock_query():\n",
    "    #url = 'main code url'\n",
    "    #stock_ticker = requests.get('stock ticker')\n",
    "    \n",
    "    stock_ticker = input(\"Stock: \")\n",
    "    start_date = input(\"DD/MM/YY: \")\n",
    "    end_date = input(\"DD/MM/YY: \")\n",
    "    price_change = input(\"Price change trigger %: \")\n",
    "    volume_index = input(\"Volume trigger in millions: \")\n",
    "    \n",
    "    datetime_start = datetime.strptime(start_date, '%d/%m/%y')\n",
    "    datetime_end = datetime.strptime(end_date, '%d/%m/%y')\n",
    "    price_change = float(price_change)/100\n",
    "    volume_index = float(volume_index)*1000000\n",
    "\n",
    "# open file with filename matching user input\n",
    "\n",
    "    file_input = stock_ticker\n",
    "    if not \".csv\" in stock_ticker:\n",
    "        file_input += \".csv\"\n",
    "    stock_df = pd.read_csv(file_input)\n",
    "\n",
    "    stock_df['Date'] = pd.to_datetime(stock_df['Date']) \n",
    "    mask = (stock_df['Date'] > datetime_start) & (stock_df['Date'] <= datetime_end)\n",
    "    period_df = stock_df.loc[mask]\n",
    "\n",
    "# perform calculations on file\n",
    "\n",
    "# get dates that satisfy price change criteria\n",
    "    period_df['Date'] = period_df['Date'].dt.date\n",
    "    period_df['Price Change'] = period_df.High / period_df.Low - 1\n",
    "    period_df.loc[period_df['Price Change'] >= price_change, 'Price Change Date'] = period_df.Date \n",
    "    period_df.loc[period_df['Price Change'] < price_change, 'Price Change Date'] = ''\n",
    "    \n",
    "# get dates that satisfy volume criteria\n",
    "    period_df.loc[period_df['Volume'] >= volume_index, 'Volume Index Date'] = period_df.Date \n",
    "    period_df.loc[period_df['Volume'] < volume_index, 'Volume Index Date'] = '' \n",
    "\n",
    "# save dates in 2 csv files, 1 for price change and 1 for volume index\n",
    "    price_change_dates_df = period_df[['Price Change','Price Change Date']].copy()\n",
    "    filter = price_change_dates_df['Price Change Date'] != \"\"\n",
    "    price_change_dates_df = price_change_dates_df[filter]\n",
    "    price_change_dates_df.to_csv('pricechangetest.csv')\n",
    "    \n",
    "    volume_index_dates_df = period_df[['Volume','Volume Index Date']].copy()\n",
    "    filter = volume_index_dates_df['Volume Index Date'] != \"\"\n",
    "    volume_index_dates_df = volume_index_dates_df[filter]\n",
    "    volume_index_dates_df.to_csv('volumeindextest.csv')\n",
    "\n",
    "stock_query()\n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
