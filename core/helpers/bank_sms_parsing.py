#!/usr/bin/env python
# coding: utf-8

# # BRAC

# ## Card Payment

# In[111]:


# keyword: card payment

# dummy text
# text = "BDT 900 transacted at LAZZ PHARMA on 19/07/20 [07:09:21 PM BST] using Card#**1305. Available balance: BDT 3,675.08. Helpline 16221"

def check_brac_card_payment(text):
  # import libraries
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # card purchase pattern
  card_payment_pattern = r'BDT (\d+\.\d{2}|\d+) transacted[^\.]+using Card'

  # check if txn is credited by initializing a boolean
  card_payment = bool(re.search(card_payment_pattern, text))

  # card payment amount
  card_payment_amount = None
  if card_payment == True:
    # check the amount
    try:
      amount_pattern = card_payment_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Card purchase', amount)
      card_payment_amount = amount
    except:
      pass
  
  return card_payment_amount

# print(check_brac_card_payment(text))


# # DBBL

# ## Debited

# In[112]:


# keyword: debited

# dummy text
# text = "debited by BDT 20,000fadf "

def check_dbbl_debit(text):
  # import libraries
  import pandas as pd
  import re

  # remove the commas that may appear with txn amount numbers
  text = text.replace(',', '')


  # debited_pattern
  debited_pattern = r'debited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is debited by initializing a boolean
  debited = bool(re.search(debited_pattern, text))

  # debited txn amount
  debited_amount = None
  if debited == True:
    # check the amount 
    try:
      amount_pattern = debited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Debited', amount)
      debited_amount = amount
    except:
      pass

  return debited_amount

# print(check_dbbl_debit(text))


# ## Credited

# In[113]:


# keyword: credited

# dummy text
# text = "Dear Sir, your DBBL A/C ***9788 credited by BDT 45,000.00 on 08-07-2020 09:48:57 AM.Enjoy shopping with your Debit Card.Call 16216"

def check_dbbl_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'credited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_dbbl_credit(text))


# ## Interest Credit

# In[114]:


# keyword: credited

# dummy text
# text = "Dear Sir, your DBBL A/C ***6654 credited (Interest Credit) by BDT 1.98 on 01-07-2020 04:15:24 AM.Please Download NexusPay https://bit.ly/nexuspay .Call 16216"

def check_dbbl_interest_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  interest_credit_pattern = r'credited[^\.]+?Interest Credit[^\.]+?[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  interest_credit = bool(re.search(interest_credit_pattern, text))

  # credited txn amount
  interest_credit_amount = None
  if interest_credit == True:
    # check the amount
    try:
      amount_pattern = interest_credit_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      interest_credit_amount = amount
    except:
      pass

  return interest_credit_amount

# print(check_dbbl_interest_credit(text))


# ## Fund Transfer In

# In[115]:


# keyword: Fund Transfer (In)

# dummy text
# text5 = "Tk2000.00 received from A/C:102010201 Fee:Tk0, Your A/C Balance: Tk3623.87 TxnId:1829598802 Date:13-JUL-20 01:27:27 pm. Download https://bit.ly/nexuspay"
# text9 = "Dear Sir, your DBBL A/C ***6654 credited (NPSB Internet Banking Fund Transfer) by BDT 500.00 on 14-06-2020 12:58:53 PM.Please Download NexusPay https://bit.ly/"
# text11 = "Tk500.00 transferred to A/C:102010103 Fee:Tk4.50, Your A/C Balance: Tk39.00 TxnId:1811576627 Date:02-JUL-20 11:56:18 am. Download https://bit.ly/nexuspay"

# dummy text
# text = text11

def check_dbbl_fund_transfer_in(text):

  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # Fund Transfer (in) pattern
  fund_transfer_in_pattern1 = r'Tk(\d+\.\d{2}|\d+)[^\.]+received from'
  fund_transfer_in_pattern2 = r'credited[^\.]+NPSB Internet Banking Fund Transfer[^\.]+BDT[\s](\d+\.\d{2}|\d+)'
  fund_transfer_in_pattern3 = r'Tk(\d+\.\d{2}|\d+)[^\.]+transferred to'

  # check if txn is Fund Transfer (in) and find transaction amount
  fund_transfer_in_amount = None
  if bool(re.search(fund_transfer_in_pattern1, text)) == True:
    # check the amount 
    try:
      amount_pattern = fund_transfer_in_pattern1
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer In', amount)
      fund_transfer_in_amount = amount
    except:
      pass
  elif bool(re.search(fund_transfer_in_pattern2, text)) == True:
    # check the amount
    try:
      amount_pattern = fund_transfer_in_pattern2
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer In', amount)
      fund_transfer_in_amount = amount
    except:
      pass 
  elif bool(re.search(fund_transfer_in_pattern3, text)) == True:
    # check the amount
    try:
      amount_pattern = fund_transfer_in_pattern3
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer In', amount)
      fund_transfer_in_amount = amount
    except:
      pass

  return fund_transfer_in_amount

# print(check_dbbl_fund_transfer_in(text))


# ## Fund Transfer Out

# In[116]:


# Keyword: Fund Transfer Out

# dummy text
# text7 = "Tk15,00.00 transferred to A/C:205010801 Fee:Tk.00, Your A/C Balance: Tk1500.87 TxnId:1839736232 Date:20-JUL-20 06:53:47 am. Download https://bit.ly/nexuspay"
# text8 = "Dear Sir, your DBBL A/C ***6654 debited (Fund Transfer Debit) by BDT 60.00 on 04-07-2020 08:11:07 PM.Please Download NexusPay https://bit.ly/nexuspay .Call 162"
# text10 = "Dear Sir, your DBBL A/C ***6654 debited(EFT Dr- By PAYABLE FOR EFTN 826758-30300-CCD ) by BDT 148.80 on 28-01-2020 04:28:02 PM.Please Download NexusPay https:/"

# text = text10

def check_dbbl_fund_transfer_out(text):

  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # Fund Transfer (in) pattern
  fund_transfer_out_pattern1 = r'Tk(\d+\.\d{2}|\d+)[^\.]+transferred to'
  fund_transfer_out_pattern2 = r'debited[^\.]+Fund Transfer Debit[^\.]+BDT[\s](\d+\.\d{2}|\d+)'
  fund_transfer_out_pattern3 = r'EFT Dr-[^\.]+BDT[\s](\d+.\d{2}|\d+)'

  # check if txn is Fund Transfer (in) and find transaction amount
  fund_transfer_out_amount = None
  if bool(re.search(fund_transfer_out_pattern1, text)) == True:
    # check the amount 
    try:
      amount_pattern = fund_transfer_out_pattern1
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass
  elif bool(re.search(fund_transfer_out_pattern2, text)) == True:
    # check the amount
    try:
      amount_pattern = fund_transfer_out_pattern2
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass 
  elif bool(re.search(fund_transfer_out_pattern3, text)) == True:
    # check the amount
    try:
      amount_pattern = fund_transfer_out_pattern3
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass

  return fund_transfer_out_amount

# print(check_dbbl_fund_transfer_out(text))


# ## Cash Out/Withdrawal

# In[117]:


# keyword: Cash-Out

# dummy text
# text = "Cash-Out from ATM Tk10,00.00Fee:Tk Your A/C Balance: Tk15.87.TxnId:1841272889Date:19-JUL-20 08:18:39 am. Please download https://bit.ly/nexuspay"

def check_dbbl_withdrawal(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with amount values
  text = text.replace(',', '')

  # Cash-Out pattern
  cash_out_pattern = r'Cash-Out[^\.]+Tk(\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  cash_out = bool(re.search(cash_out_pattern, text))

  # cash-out txn amount
  cash_out_amount = None
  if cash_out == True:
    # check the amount
    try:
      amount_pattern = cash_out_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      cash_out_amount = amount
    except:
      pass

  return cash_out_amount

# print(check_dbbl_withdrawal(text))


# ## Balance

# In[118]:


# keyword: Balance/Monthend balance

# dummy text
# text6 = "Dear Sir,Jun-20 Monthend balance of DBBL AC: ***2361 is BDT 5.00.Accumulated reward point:0.Don't share your PIN/Verification Code with anyone."
# text5 = "Tk2000.00 received from A/C:102010201 Fee:Tk0, Your A/C Balance: Tk3623.87 TxnId:1829598802 Date:13-JUL-20 01:27:27 pm. Download https://bit.ly/nexuspay"
# text7 = "Tk15,00.00 transferred to A/C:205010801 Fee:Tk.00, Your A/C Balance: Tk1500.87 TxnId:1839736232 Date:20-JUL-20 06:53:47 am. Download https://bit.ly/nexuspay"

# text = text7

def check_dbbl_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern1 = r'Monthend balance[^\.]+BDT[\s](\d+\.\d{2}|\d+)'
  balance_pattern2 = r'Your A/C Balance:[^\.]+Tk(\d+\.\d{2}|\d+)'

  # check if txn has balance info and find balance amount
  balance_amount = None
  if bool(re.search(balance_pattern1, text)) == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern1
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  elif bool(re.search(balance_pattern2, text)) == True:
    # check the amount
    try:
      amount_pattern = balance_pattern2
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass 

  return balance_amount

# print(check_dbbl_balance(text))


# # Pubali Bank

# ## Debited

# In[119]:


# keyword: debited

# dummy text
# text = "Your account 0549****0059 has been debited with BDT 86.25 for issuing the cheque book. Your acc balance is BDT 5918.19.Thank you. OBL Helpline 16269"

def check_pubali_debit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # debited pattern
  debited_pattern = r'debited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  debited = bool(re.search(debited_pattern, text))

  # cash-out txn amount
  debited_amount = None
  if debited == True:
    # check the amount
    try:
      amount_pattern = debited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      debited_amount = amount
    except:
      pass

  return debited_amount

# print(check_pubali_debit(text))


# ## Cash Out/Withdrawal

# In[120]:


# keyword: withdrawn

# dummy text
# text = "You withdrawn BDT 20000.00 through ATM from 28/A NAYAPALTAN using Card Number **1103 on 18-JUN-20 .A/C Bal:Cr 31580.36."

def check_pubali_withdrawal(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # debited pattern
  withdrawal_pattern = r'withdrawn[^\.]+BDT[\s](\d+\.\d{2}|\d+)[^\.]+ATM'

  # check if txn is Cash-Out by initializing a boolean
  withdrawal = bool(re.search(withdrawal_pattern, text))

  # cash-out txn amount
  withdrawal_amount = None
  if withdrawal == True:
    # check the amount
    try:
      amount_pattern = withdrawal_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      withdrawal_amount = amount
    except:
      pass

  return withdrawal_amount

# print(check_pubali_withdrawal(text))


# ## Balance

# In[121]:


# keyword: balance

# dummy text
# text1 = "Your account 0549****0059 has been debited with BDT 86.25 for issuing the cheque book. Your acc balance is BDT 5918.19.Thank you. OBL Helpline 16269"
# text2 = "You withdrawn BDT 20000.00 through ATM from 28/A NAYAPALTAN using Card Number **1103 on 18-JUN-20 .A/C Bal:Cr 31580.78."

# text = text2 

def check_pubali_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern1 = r'acc balance[^\.]+BDT[\s](\d+\.\d{2}|\d+)'
  balance_pattern2 = r'Bal:[^\.]+[\s](\d+\.\d{2}|\d+)'

  # check if txn has balance info and find balance amount
  balance_amount = None
  if bool(re.search(balance_pattern1, text)) == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern1
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  elif bool(re.search(balance_pattern2, text)) == True:
    # check the amount
    try:
      amount_pattern = balance_pattern2
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass 

  return balance_amount

# print(check_pubali_balance(text))


# # Premier Bank

# ## Debited

# In[122]:


# keyword: debited

# dummy text
# text = "Your account number **** has been debited with BDT 563.78 on 13-07-20 03.51.56. Available balance BDT 999.99 For more Info Call 16411"

def check_premier_debit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # debited pattern
  debited_pattern = r'debited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  debited = bool(re.search(debited_pattern, text))

  # cash-out txn amount
  debited_amount = None
  if debited == True:
    # check the amount
    try:
      amount_pattern = debited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      debited_amount = amount
    except:
      pass

  return debited_amount

# print(check_premier_debit(text))


# ## Credited

# In[123]:


# keyword: credited

# dummy text
# text = "Your account number **** has been credited with BDT 6000.50 on 21-07-20 03.21.15. Available balance BDT 10000.98 For more Info Call 16411"

def check_premier_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'credited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_premier_credit(text))


# ## Balance

# In[124]:


# keyword: Balance

# dummy text
# text = "Your account number **** has been debited with BDT 658.11 on 13-07-20 03.51.56. Available balance BDT 987.56 For more Info Call 16411"

def check_premier_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'Available balance[\s]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn has balance info by initializing a boolean
  balance = bool(re.search(balance_pattern, text))

  # check if txn is Fund Transfer (in) and find transaction amount
  if balance == True:
    # check the amount
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      balance_amount = amount
    except:
      pass 

  return balance_amount

# print(check_premier_balance(text))


# # EBL

# ## Credited

# In[125]:


# keyword: credited

# dummy text
# text = "AC 111***828 is credited with BDT 230.34 as Fund Transfer on 13-Aug-2020 05:49:22 PM. Balance is BDT 1093.15. Thanks. EBL Helpline 16230"

def check_ebl_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'credited[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_ebl_credit(text))


# ## Card Purchase

# In[126]:


# keyword: card purchase

# dummy text
# text = "EBL CARDS: Purchase txn BDT 1152.98 from EVALY.COM Jigatala TSO BD. Card ****** on 22-Jul-20 10:31:38 AM BST. Balance: BDT 539.97. EBL Helpline 16230"

def check_ebl_card_purchase(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # card purchase pattern
  card_purchase_pattern = r'EBL CARDS: Purchase txn BDT (\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  card_purchase = bool(re.search(card_purchase_pattern, text))

  # credited txn amount
  card_purchase_amount = None
  if card_purchase == True:
    # check the amount
    try:
      amount_pattern = card_purchase_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Card purchase', amount)
      card_purchase_amount = amount
    except:
      pass

  return card_purchase_amount

# print(check_ebl_card_purchase(text))


# ## Card Payment

# In[127]:


# keyword: card payment

# dummy text
# text = "EBL CARDS: Payment of BDT 430.54 credited to Card *** on 16-Jul-20 09:28:01 PM. Balance: BDT 900.56. Thank You. EBL Helpline 16230"

def check_ebl_card_payment(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # card purchase pattern
  card_payment_pattern = r'EBL CARDS: Payment[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is credited by initializing a boolean
  card_payment = bool(re.search(card_payment_pattern, text))

  # credited txn amount
  card_payment_amount = None
  if card_payment == True:
    # check the amount
    try:
      amount_pattern = card_payment_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Card purchase', amount)
      card_payment_amount = amount
    except:
      pass

  return card_payment_amount

# print(check_ebl_card_payment(text))


# ## Fund Transfer In

# In[128]:


# keyword: Fund Transfer (in)

# dummy text
# text = "AC 111***323 is credited with BDT 230.23 as Fund Transfer on 13-Aug-20 05:49:22 PM. Balance is BDT 1093.15. Thanks. EBL Helpline 16230"

def check_ebl_fund_transfer_in(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # Fund Transfer (in) pattern
  fund_transfer_in_pattern = r'credited with BDT (\d+\.\d{2}|\d+) as Fund Transfer'

  # check if txn is Fund Transfer (in) and 
  fund_transfer_in = bool(re.search(fund_transfer_in_pattern, text))

  # find transaction amount
  if bool(re.search(fund_transfer_in_pattern, text)) == True:
    # check the amount 
    try:
      amount_pattern = fund_transfer_in_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer In', amount)
      fund_transfer_in_amount = amount
    except:
      pass

  return fund_transfer_in_amount

# print(check_ebl_fund_transfer_in(text))


# ## Fund Transfer Out

# In[129]:


# Keyword: Fund Transfer Out

# dummy text
# SMS3 = 'EBL CARDS: NPSB Fund Transfer BDT 897.56 using Card **** on 14-Jul-20 11:55:50 AM.Your A/C **** Balance BDT 10500.45. Thank You. EBL Helpline 16230'
# SMS6 = 'AC **** is debited with BDT 1152 as Fund Transfer Through SkyBanking on 16-Jul-20 09:24:32 PM. Balance is BDT 75.26. Thanks. EBL Helpline 16230'

# text = SMS6

def check_ebl_fund_transfer_out(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # Fund Transfer (in) pattern
  fund_transfer_out_pattern1 = r'EBL CARDS:[^\.]+Fund Transfer BDT (\d+\.\d{2}|\d+)'
  fund_transfer_out_pattern2 = r'debited with BDT (\d+\.\d{2}|\d+) as Fund Transfer'

  # check if txn is Fund Transfer (in) and find transaction amount
  fund_transfer_out_amount = None
  if bool(re.search(fund_transfer_out_pattern1, text)) == True:
    # check the amount 
    try:
      amount_pattern = fund_transfer_out_pattern1
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass
  elif bool(re.search(fund_transfer_out_pattern2, text)) == True:
    # check the amount
    try:
      amount_pattern = fund_transfer_out_pattern2
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass 

  return fund_transfer_out_amount

# print(check_ebl_fund_transfer_out(text))


# ## Cash Out/Withdrawal

# In[130]:


# keyword: cash out/withdrawal

# dummy text
# SMS7 = 'Cash WD BDT1000 from EBL BASUNDHARA R.A A. Card **** on 08-Jul-20 07:29:01 PM BST.Your A/C **** Balance BDT 5000.47. EBL Helpline 16230'

# text = SMS7

def check_ebl_withdrawal(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with amount values
  text = text.replace(',', '')

  # Cash-Out pattern
  cash_out_pattern = r'Cash WD BDT(\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  cash_out = bool(re.search(cash_out_pattern, text))

  # cash-out txn amount
  cash_out_amount = None
  if cash_out == True:
    # check the amount
    try:
      amount_pattern = cash_out_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      cash_out_amount = amount
    except:
      pass

  return cash_out_amount

# print(check_ebl_withdrawal(text))


# ## Balance

# In[131]:


# keyword: Balance/Monthend balance

# dummy text
# SMS1 = 'AC 111***828 is credited with BDT 230 as Fund Transfer on 13-Aug-2020 05:49:22 PM. Balance is BDT 1093.15. Thanks. EBL Helpline 16230'
# SMS2 = 'EBL CARDS: Purchase txn BDT 1152 from EVALY.COM Jigatala TSO BD. Card ****** on 22-Jul-20 10:31:38 AM BST. Balance: BDT 539.97. EBL Helpline 16230'
# SMS3 = 'EBL CARDS: NPSB Fund Transfer BDT 897.56 using Card **** on 14-Jul-20 11:55:50 AM.Your A/C **** Balance BDT 10500.45. Thank You. EBL Helpline 16230'

# text = SMS3

def check_ebl_balance(text):
  # import libraries
  import pandas as pd
  import re
  import json

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'Balance[^\.]+BDT (\d+\.\d{2}|\d+)'

  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))

  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount

# print(check_ebl_balance(text))


# # AIBL

# ## Deposit

# In[132]:


# keyword: deposit

# dummy text
# SMS1 = "Dear Customer, Tk. 4000 has been Cash Received to A/C# 121112****8 on 13-JUL-19, 01:20:44 PM. Thanks for banking with AIBL."

# text = SMS1

def check_aibl_deposit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # deposit pattern
  deposit_pattern = r'Tk. (\d+\.\d{2}|\d+) has been Cash Received to'

  # check if txn has deposit info 
  deposit = bool(re.search(deposit_pattern, text))

  # find deposit amount
  if deposit == True:
    # check the amount 
    try:
      amount_pattern = deposit_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      deposit_amount = amount
    except:
      pass
  
  return deposit_amount

# print(check_aibl_deposit(text))


# ## Debit

# In[133]:


# keyword: deposit

# dummy text
# SMS1 = "Dear Customer, Tk. 10000 has been Clearing Debit from A/C# 121112****8 on 08-JUL-20, 01:48:00 PM. Thanks for banking with AIBL."

# text = SMS1

def check_aibl_debit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # deposit pattern
  debit_pattern = r'Tk. (\d+\.\d{2}|\d+) has been Clearing Debit from'

  # check if txn has deposit info 
  debit = bool(re.search(debit_pattern, text))

  # find deposit amount
  if debit == True:
    # check the amount 
    try:
      amount_pattern = debit_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      debit_amount = amount
    except:
      pass
  
  return debit_amount

# print(check_aibl_debit(text))


# ## Credit

# In[134]:


# keyword: credited

# dummy text
# text = "Dear Customer, Tk 1350 has been credited in your a/c 2072****290 BR KARWAN BAZAR on 02-Jul-2020.Current balance is Tk 3095.73 Helpline:16474"

def check_aibl_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'Tk (\d+\.\d{2}|\d+)[^\.]+credited'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_aibl_credit(text))


# ## Balance

# In[135]:


# keyword: Balance/Monthend balance

# dummy text
# SMS1 = 'Dear Customer, Tk 1350 has been credited in your a/c 2072****290 BR KARWAN BAZAR on 02-Jul-2020.Current balance is Tk 3095.73 Helpline:16474'

# text = SMS1

def check_aibl_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'balance[^\.]+Tk (\d+\.\d{2}|\d+)'

  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))

  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount

# print(check_aibl_balance(text))


# # City Bank

# ## Deposit

# In[136]:


# keyword: deposit

# dummy text
# SMS1 = "06-Jul-2020 Tk 150 Dep Tk 7,290 Bal A/C No. 225***001"

# text = SMS1

def check_city_deposit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # deposit pattern
  deposit_pattern = r'Tk (\d+\.\d{2}|\d+) Dep'

  # check if txn has deposit info 
  deposit = bool(re.search(deposit_pattern, text))

  # find deposit amount
  if deposit == True:
    # check the amount 
    try:
      amount_pattern = deposit_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      deposit_amount = amount
    except:
      pass
  
  return deposit_amount

# print(check_city_deposit(text))


# ## Card Payment

# In[137]:


# keyword: card payment

# dummy text
# text = "05-JUL-20 Tk. 8,049.42 payment received CARD NO: 376***636 Client ID: 859360"

def check_city_card_payment(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # card purchase pattern
  card_payment_pattern = r'Tk\. (\d+\.\d{2}|\d+) payment received CARD'

  # check if txn is credited by initializing a boolean
  card_payment = bool(re.search(card_payment_pattern, text))

  # credited txn amount
  card_payment_amount = None
  if card_payment == True:
    # check the amount
    try:
      amount_pattern = card_payment_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Card purchase', amount)
      card_payment_amount = amount
    except:
      pass

  return card_payment_amount

# print(check_city_card_payment(text))


# ## Cash Out/Withdrawal

# In[138]:


# keyword: cash out/withdrawal

# dummy text
# SMS7 = '05-Jul-2020 Tk 198 Wdl Tk 7,140 Bal A/C No. 225***001'

# text = SMS7

def check_city_withdrawal(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with amount values
  text = text.replace(',', '')

  # Cash-Out pattern
  cash_out_pattern = r'Tk (\d+\.\d{2}|\d+) Wdl'

  # check if txn is Cash-Out by initializing a boolean
  cash_out = bool(re.search(cash_out_pattern, text))

  # cash-out txn amount
  cash_out_amount = None
  if cash_out == True:
    # check the amount
    try:
      amount_pattern = cash_out_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      cash_out_amount = amount
    except:
      pass

  return cash_out_amount

# print(check_city_withdrawal(text))


# ## Balance

# In[139]:


# keyword: Balance/Monthend balance

# dummy text
# SMS1 = '06-Jul-2020 Tk 150 Dep Tk 7,290 Bal A/C No. 225***001'

# text = SMS1

def check_city_balance(text):
  # import libraries
  import pandas as pd
  import re
  import json

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'Tk (\d+\.\d{2}|\d+) Bal'

  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))

  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount

# print(check_city_balance(text))


# # NRBC

# ## Debited

# In[140]:


# keyword: debited

# dummy text
# text = "Dear Customer, BDT 20000 has been Debited from your A/C No. 0101319##0006 on 22/07/2020 from NRBC Planet and Balance is BDT 18032.73."

def check_nrbc_debit(text):
  # import libraries
  import pandas as pd
  import re

  # remove the commas that may appear with txn amount numbers
  text = text.replace(',', '')


  # debited_pattern
  debited_pattern = r'BDT[\s](\d+\.\d{2}|\d+)[^\.]+Debited'

  # check if txn is debited by initializing a boolean
  debited = bool(re.search(debited_pattern, text))

  # debited txn amount
  debited_amount = None
  if debited == True:
    # check the amount 
    try:
      amount_pattern = debited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Debited', amount)
      debited_amount = amount
    except:
      pass

  return debited_amount

# print(check_nrbc_debit(text))


# ## Credited

# In[141]:


# keyword: credited

# dummy text
# text = "Dear Customer, BDT 17459 has been Credited to your A/C No. 0101319##0040 on 07/08/2019 from LAKSAM BRANCH and Balance is BDT 17835.67. Nrbc"

def check_nrbc_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'BDT[\s](\d+\.\d{2}|\d+)[^\.]+Credited'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_nrbc_credit(text))


# ## Balance

# In[142]:


# keyword: Balance/Monthend balance

# dummy text
# SMS1 = 'Dear Customer, BDT 20000 has been Debited from your A/C No. 0101319##0006 on 22/07/2020 from NRBC Planet and Balance is BDT 18032.73.'
# SMS2 = 'Dear Customer, BDT 17459 has been Credited to your A/C No. 0101319##0040 on 07/08/2019 from LAKSAM BRANCH and Balance is BDT 17835.67. Nrbc'

# text = SMS2

def check_nrbc_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'Balance is BDT (\d+\.\d{2}|\d+)'

  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))

  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount

# print(check_nrbc_balance(text))


# # AB Bank

# ## Cash Out/Withdrawal

# In[143]:


# keyword: cash out/withdrawal

# dummy text
# SMS7 = 'Dear Customer, AB Bank ATM Cash Transaction of BDT 1000 debited from A/C 4005***303 at 2020-06-08 14:09. Balance: BDT 22617.62. Helpline 16207.'

# text = SMS7

def check_ab_withdrawal(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with amount values
  text = text.replace(',', '')

  # Cash-Out pattern
  cash_out_pattern = r'ATM Cash[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  cash_out = bool(re.search(cash_out_pattern, text))

  # cash-out txn amount
  cash_out_amount = None
  if cash_out == True:
    # check the amount
    try:
      amount_pattern = cash_out_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      cash_out_amount = amount
    except:
      pass

  return cash_out_amount

# print(check_ab_withdrawal(text))


# ## Bank_to_Mobile_Recharge

# In[144]:


# keyword: bank_to_mobile_recharge

# dummy text
# SMS7 = 'Dear Customer, Top up(IB) Transaction of BDT 198 debited from A/C 4005***303 at 2020-03-25 14:47. Balance: BDT 3992.62.'

# text = SMS7

def check_ab_bank_to_mobile_recharge(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with amount values
  text = text.replace(',', '')

  # Cash-Out pattern
  bank_to_mobile_recharge_pattern = r'Top up[^\.]+BDT[\s](\d+\.\d{2}|\d+)'

  # check if txn is Cash-Out by initializing a boolean
  bank_to_mobile_recharge = bool(re.search(bank_to_mobile_recharge_pattern, text))

  # cash-out txn amount
  bank_to_mobile_recharge_amount = None
  if bank_to_mobile_recharge == True:
    # check the amount
    try:
      amount_pattern = bank_to_mobile_recharge_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Cash Out', amount)
      bank_to_mobile_recharge_amount = amount
    except:
      pass

  return bank_to_mobile_recharge_amount

# print(check_ab_bank_to_mobile_recharge(text))


# ## Interest Credit

# In[145]:


# keyword: interest credit

# dummy text
# text = 'Dear Customer, Interest Transaction of BDT 155.43 credited to A/C 4005***303 at 2020-07-01 03:04. Balance: BDT 44627.05.'

def check_ab_interest_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  interest_credit_pattern = r'Interest Transaction[^\.]+BDT[\s](\d+\.\d{2}|\d+)[^\.]+credited'

  # check if txn is credited by initializing a boolean
  interest_credit = bool(re.search(interest_credit_pattern, text))

  # credited txn amount
  interest_credit_amount = None
  if interest_credit == True:
    # check the amount
    try:
      amount_pattern = interest_credit_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      interest_credit_amount = amount
    except:
      pass

  return interest_credit_amount

# print(check_ab_interest_credit(text))


# ## Fund Transfer Out

# In[146]:


# Keyword: Fund Transfer Out

# dummy text

# text = "Dear Customer, Fund Transfer(IB) Transaction of BDT 5000 debited from A/C 4005***303 at 2020-06-14 15:08. Balance: BDT 17319.62. Helpline 16207."

def check_ab_fund_transfer_out(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # Fund Transfer (in) pattern
  fund_transfer_out_pattern = r'Fund Transfer[^\.]+BDT[\s](\d+\.\d{2}|\d+)[^\.]+debited'


  # check if txn is Fund Transfer (in) and find transaction amount
  fund_transfer_out_amount = None
  if bool(re.search(fund_transfer_out_pattern, text)) == True:
    # check the amount 
    try:
      amount_pattern = fund_transfer_out_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Fund Transfer Out', amount)
      fund_transfer_out_amount = amount
    except:
      pass

  return fund_transfer_out_amount

# print(check_ab_fund_transfer_out(text))


# ## Credited

# In[147]:


# keyword: credited

# dummy text
# text = "Dear Customer, Transaction of BDT 1000 credited to A/C 4005***303 at 2020-04-29 12:18. Balance: BDT 28847.62."

def check_ab_credit(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas that may be associated with numbers
  text = text.replace(',', '')

  # credited pattern
  credited_pattern = r'BDT[\s](\d+\.\d{2}|\d+)[^\.]+?credited'

  # check if txn is credited by initializing a boolean
  credited = bool(re.search(credited_pattern, text))

  # credited txn amount
  credited_amount = None
  if credited == True:
    # check the amount
    try:
      amount_pattern = credited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Credited', amount)
      credited_amount = amount
    except:
      pass

  return credited_amount

# print(check_ab_credit(text))


# ## Balance

# In[148]:


# keyword: Balance/Monthend balance

# dummy text
# SMS1 = 'Dear Customer, Transaction of BDT 1000 credited to A/C 4005***303 at 2020-04-29 12:18. Balance: BDT 28847.62.'
# SMS2 = 'Dear Customer, Fund Transfer(IB) Transaction of BDT 5000 debited from A/C 4005***303 at 2020-06-14 15:08. Balance: BDT 17319.62. Helpline 16207.'

# text = SMS2

def check_ab_balance(text):
  # import libraries
  import pandas as pd
  import re

  # remove commas in numbers
  text = text.replace(',', '')

  # balance pattern
  balance_pattern = r'Balance: BDT (\d+\.\d{2}|\d+)'

  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))

  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount

# print(check_ab_balance(text))


# # UCB

# ## Debited

# In[149]:


# keyword: debited
 
# dummy text
# text = "Your a/c (XXXXXXXXXXXX5705) has been Debited BDT 25,330.00. Available Balance is BDT 21,734.80 at 20Jul2020 12:51 PM. Thank you."
 
def check_ucb_debit(text):
  # import libraries
  import pandas as pd
  import re
 
  # remove the commas that may appear with txn amount numbers
  text = text.replace(',', '')
 
 
  # debited_pattern
  debited_pattern = r'Debited[^\.]+?BDT[\s](\d+\.\d{2}|\d+)'
 
  # check if txn is debited by initializing a boolean
  debited = bool(re.search(debited_pattern, text))
 
  # debited txn amount
  debited_amount = None
  if debited == True:
    # check the amount 
    try:
      amount_pattern = debited_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Debited', amount)
      debited_amount = amount
    except:
      pass
 
  return debited_amount
 
# print(check_ucb_debit(text))


# ## Card Payment

# In[150]:


# keyword: card payment
 
# dummy text
# text = "Dear C/H,Thank you for payment BDT 30000.00 against your UCB Card# 0168 (ID# 558797)"
 
def check_ucb_card_payment(text):
  # import libraries
  import pandas as pd
  import re
 
  # remove commas that may be associated with numbers
  text = text.replace(',', '')
 
  # card purchase pattern
  card_payment_pattern = r'payment[^\.]+?BDT[\s](\d+\.\d{2}|\d+)[^\.]+?UCB Card'
 
  # check if txn is credited by initializing a boolean
  card_payment = bool(re.search(card_payment_pattern, text))
 
  # credited txn amount
  card_payment_amount = None
  if card_payment == True:
    # check the amount
    try:
      amount_pattern = card_payment_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Card purchase', amount)
      card_payment_amount = amount
    except:
      pass
 
  return card_payment_amount
 
# print(check_ucb_card_payment(text))


# ## Balance

# In[151]:


# keyword: Balance/Monthend balance
 
# dummy text
# SMS2 = 'Your a/c (XXXXXXXXXXXX5705) has been Debited BDT 25,330.00. Available Balance is BDT 21,734.80 at 20Jul2020 12:51 PM. Thank you.'
 
# text = SMS2
 
def check_ucb_balance(text):
  # import libraries
  import pandas as pd
  import re
 
  # remove commas in numbers
  text = text.replace(',', '')
 
  # balance pattern
  balance_pattern = r'Available Balance[^\.]+?BDT[\s](\d+\.\d{2}|\d+)'
 
  # check if txn has balance info and 
  balance = bool(re.search(balance_pattern, text))
 
  # find balance amount
  if balance == True:
    # check the amount 
    try:
      amount_pattern = balance_pattern
      amount = re.findall(amount_pattern, text)[0]
      # print('Balance', amount)
      balance_amount = amount
    except:
      pass
  
  return balance_amount
 
# print(check_ucb_balance(text))


# # Parse

# In[158]:


def parse_sms_data(data):
  # import pandas and json
  import pandas as pd
  import json
  import datetime
  from dateutil.relativedelta import relativedelta
 
 
  # as a precaution, replace single quotes with double quotes
  string = data.replace("'", '"').replace('\n', '').replace('\r', '').replace('\f', '').replace('\t', '').replace('\v', '')
 
  # initialize the string as as json string object
  string = json.loads(string)
 
  # initialize json object as a dataframe
  data = pd.DataFrame(string)
  # check if you have to 
  # data.head()
 
  # reset index
  data = data.reset_index(drop=True)

  # convert data type of date to turn integer values into actual timestamp values
  data['date'] = data['date'].astype(int)

  # run a loop to change all date integer values to actual timestamp values
  for i in range(len(data)):
    data.loc[i, 'date'] = datetime.datetime.fromtimestamp(data.loc[i, 'date'] / 1e3) 

  # initialize start and end dates for which you will filter the dataset
  start_date = datetime.datetime.today()
  end_date = start_date + relativedelta(months=-3)

  # create a mask for filtering within the date range
  mask = (data['date'] <= start_date) & (data['date'] > end_date) 

  # filter the dataset using the mask for the date range
  data = data[mask] 
 
  # initialize columns that we are going to scrape information about from the texts
  data['debit'] = None
  data['credit'] = None
  data['withdrawal'] = None
  data['card_payment'] = None
  data['card_purchase'] = None
  data['interest_credit'] = None
  data['deposit'] = None
  data['bank_to_mobile_recharge'] = None 
  data['balance'] = None
  data['fund_transfer_in'] = None
  data['fund_transfer_out'] = None 
 
  # Check DBBL
  for i in range(len(data)):
    # check if the text is from DBBL and fill the columns accordingly
    if data.loc[i, 'address'] == '16216':
      data.loc[i, 'debit'] = check_dbbl_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = check_dbbl_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = check_dbbl_withdrawal(data.loc[i, 'body'])
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = check_dbbl_interest_credit(data.loc[i, 'body'])
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_dbbl_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = check_dbbl_fund_transfer_in(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_out'] = check_dbbl_fund_transfer_out(data.loc[i, 'body'])

    # check if the text is from BRAC and fill the columns accordingly
    elif data.loc[i, 'address'] == 'BRAC BANK':
      data.loc[i, 'debit'] = None
      data.loc[i, 'credit'] = None
      data.loc[i, 'withdrawal'] = None
      data.loc[i, 'card_payment'] = check_brac_card_payment(data.loc[i, 'body'])
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = None
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text is from Pubali and fill the columns accordingly
    elif data.loc[i, 'address'] == 'Pubali Bank':
      data.loc[i, 'debit'] = check_pubali_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = None
      data.loc[i, 'withdrawal'] = check_pubali_withdrawal(data.loc[i, 'body'])
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_pubali_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text is from Premier and fill the columns accordingly
    elif data.loc[i, 'address'] == 'PREMIER BANK':
      data.loc[i, 'debit'] = check_premier_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = check_premier_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = None
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_premier_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text if from EBL and fill the columns accordingly
    elif data.loc[i, 'address'] == 'EBL.':
      data.loc[i, 'debit'] = None
      data.loc[i, 'credit'] = check_ebl_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = check_ebl_withdrawal(data.loc[i, 'body'])
      data.loc[i, 'card_payment'] = check_ebl_card_payment(data.loc[i, 'body'])
      data.loc[i, 'card_purchase'] = check_ebl_card_purchase(data.loc[i, 'body'])
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_ebl_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = check_ebl_fund_transfer_in(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_out'] = check_ebl_fund_transfer_out(data.loc[i, 'body'])
    
    # check if the text if from AIBL and fill the columns accordingly
    elif data.loc[i, 'address'] == 'AIBL.':
      data.loc[i, 'debit'] = check_aibl_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = check_aibl_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = None
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = check_aibl_deposit(data.loc[i, 'body'])
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_aibl_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text if from City and fill the columns accordingly
    elif data.loc[i, 'address'] == 'CITY BANK':
      data.loc[i, 'debit'] = None
      data.loc[i, 'credit'] = None
      data.loc[i, 'withdrawal'] = check_city_withdrawal(data.loc[i, 'body'])
      data.loc[i, 'card_payment'] = check_city_card_payment(data.loc[i, 'body'])
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = check_city_deposit(data.loc[i, 'body'])
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_city_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text if from NRBC and fill the columns accordingly
    elif data.loc[i, 'address'] == 'NRBC BANK':
      data.loc[i, 'debit'] = check_nrbc_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = check_nrbc_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = None
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_nrbc_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
    
    # check if the text if from NRBC and fill the columns accordingly
    elif data.loc[i, 'address'] == 'AB BANK':
      data.loc[i, 'debit'] = None
      data.loc[i, 'credit'] = check_ab_credit(data.loc[i, 'body'])
      data.loc[i, 'withdrawal'] = check_ab_withdrawal(data.loc[i, 'body'])
      data.loc[i, 'card_payment'] = None
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = check_ab_interest_credit(data.loc[i, 'body'])
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = check_ab_bank_to_mobile_recharge(data.loc[i, 'body'])
      data.loc[i, 'balance'] = check_ab_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = check_ab_fund_transfer_out(data.loc[i, 'body'])
    
    # check if the text if from UCB and fill the columns accordingly
    elif (data.loc[i, 'address'] == 'UCB BANK' or data.loc[i, 'address'] == 'UCB RETAIL'):
      data.loc[i, 'debit'] = check_ucb_debit(data.loc[i, 'body'])
      data.loc[i, 'credit'] = None
      data.loc[i, 'withdrawal'] = None
      data.loc[i, 'card_payment'] = check_ucb_card_payment(data.loc[i, 'body'])
      data.loc[i, 'card_purchase'] = None
      data.loc[i, 'interest_credit'] = None
      data.loc[i, 'deposit'] = None
      data.loc[i, 'bank_to_mobile_recharge'] = None
      data.loc[i, 'balance'] = check_ucb_balance(data.loc[i, 'body'])
      data.loc[i, 'fund_transfer_in'] = None
      data.loc[i, 'fund_transfer_out'] = None
  
  # using dictionary to convert specific columns data types
  convert_dict = {'debit': float, 
                  'credit': float,
                  'withdrawal': float,
                  'card_payment': float,
                  'card_purchase': float,
                  'interest_credit': float,
                  'deposit': float,
                  'bank_to_mobile_recharge': float,
                  'balance': float,
                  'fund_transfer_in': float,
                  'fund_transfer_out': float
                } 
    
  data = data.astype(convert_dict)

  data = data.groupby(['id', 'address']).agg({
                                              'date': 'last', 'debit': 'sum', 'credit': 'sum', 'withdrawal': 'sum', 
                                              'card_payment': 'sum', 'card_purchase': 'sum', 'interest_credit': 'sum', 
                                              'deposit': 'sum', 'bank_to_mobile_recharge': 'sum', 'balance': 'last', 
                                              'fund_transfer_in': 'sum', 'fund_transfer_out': 'sum'
                                            }).reset_index()
  
  json_string = data.to_json(orient = 'records')

  return json_string


# # Test

# In[162]:


# # initialize a test raw_data sample and parse it to check
# raw_data = '''{
#   "address": [
#     "16216",
#     "16216",
#     "16216",
#     "16216"
#   ],
#   "body": [
#     "Dear Sir, your DBBL A/C ***9788 credited by BDT 45,000.00 on 08-07-2020 09:48:57 AM.Enjoy shopping with your Debit Card.Call 16216",
#     "Dear Sir, your DBBL A/C ***6654 credited (Interest Credit) by BDT 1.98 on 01-07-2020 04:15:24 AM.Please Download NexusPay https://bit.ly/nexuspay .Call 16216",
#     "Tk2000.00 received from A/C:102010201 Fee:Tk0, Your A/C Balance: Tk3623.87 TxnId:1829598802 Date:13-JUL-20 01:27:27 pm. Download https://bit.ly/nexuspay",
#     "Cash-Out from ATM Tk10,00.00Fee:Tk Your A/C Balance: Tk15.87.TxnId:1841272889Date:19-JUL-20 08:18:39 am. Please download https://bit.ly/nexuspay"
#   ],
#   "customer_id": [
#     "01677079251",
#     "01677079251",
#     "01677079251",
#     "01677079251"
#   ],
#   "date": [
#     "1598346966300",
#     "1598346153243",
#     "1598339524891",
#     "1598333712566"
#   ],
#   "id": [
#     "17241",
#     "17241",
#     "17241",
#     "17241"
#   ]
# }'''


# In[163]:


# data = parse_sms_data(raw_data)
# print(data)

