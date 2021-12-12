{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "369fbbdd-16e7-4a03-b002-99e6855e4961",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jesse\\Python\\Kaggle\\NHL\\apps\\table_playoff.py:4: UserWarning: \n",
      "The dash_table package is deprecated. Please replace\n",
      "`import dash_table` with `from dash import dash_table`\n",
      "\n",
      "Also, if you're using any of the table format helpers (e.g. Group), replace \n",
      "`from dash_table.Format import Group` with \n",
      "`from dash.dash_table.Format import Group`\n",
      "  from dash_table import DataTable, FormatTemplate\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "import dash_bootstrap_components as dbc\n",
    "from apps import table_playoff, heatmap_tab, hits_goals_tab\n",
    "from app import app\n",
    "from app import server"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0f669a01-958f-4649-830a-507dabda8fea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash app running on http://127.0.0.1:8050/\n"
     ]
    }
   ],
   "source": [
    "app.layout = dbc.Container([\n",
    "    dbc.Row([\n",
    "    dbc.Col(html.H1(\"NHL Data Jesse Sallis \" + str(pd.to_datetime('today').strftime(\"%m/%d/%Y\")), className='text-center, mb-4'),width=12)\n",
    "        ]),\n",
    "    \n",
    "    dbc.Tabs(\n",
    "            [\n",
    "                dbc.Tab(hits_goals_tab.layout,label=\"Hits/Goals by Team\"),\n",
    "                dbc.Tab(heatmap_tab.layout,label=\"Correlation Heatmap\"),\n",
    "                dbc.Tab(table_playoff.layout,label=\"Playoffs\"),\n",
    "            ],\n",
    "        ),\n",
    "    \n",
    "     html.Div(className=\"p-4\"),\n",
    "], fluid=True)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
