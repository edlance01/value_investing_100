"""
Target TGT
April 19, 2026 - 8:00pm EST by surf1680
2026	2027
Price:		127.00		EPS		8	0
Shares Out. (in M):		452		P/E		16	0
Market Cap (in $M):		58,000		P/FCF		20	0
Net Debt (in $M):		15,000		EBIT		7,000	0
TEV (in $M):		73,000		TEV/EBIT		10	0


To calculate the Return on Equity (ROE) for Target (TGT), we can use the following formula:
Net Income — bottom of the income statement (usually annual or trailing twelve months)
Shareholders' Equity — on the balance sheet (total assets minus total liabilities). Many analysts use the average of beginning and ending equity for the period to smooth out fluctuations.

"""

net_earnings = 3705
shareholders_equity = 16165

roe = net_earnings / shareholders_equity
print(f"Return on Equity (ROE): {roe:.2%}")
