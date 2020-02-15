import pandas as pd
from datetime import datetime
import sqlalchemy as sa

def fix_date(dt_string):
        if type(dt_string) != str:
            print('fix_date was passed a non-string of value {}'.format(dt_string))
            try:
                dt_string = str(dt_string)
            except:
                print('conversion of value {} of type {} to string failed'.format(dt_string, type(dt_string)))
                return None
            
        fixed_dt = None
        try:
            fixed_dt = datetime.strptime(dt_string[0:10], '%m/%d/%Y')
        except:
            pass
        if fixed_dt == None:
            try:
                fixed_dt = datetime.strptime('0{}'.format(dt_string[0:9]), '%m/%d/%Y')
            except:
                pass
        if fixed_dt == None:
            try:
                fixed_dt = datetime.strptime('{}0{}'.format(dt_string[0:3], dt_string[3:9]), '%m/%d/%Y')
            except:
                pass
        if fixed_dt == None:
            try:
                fixed_dt = datetime.strptime('0{}/0{}'.format(dt_string[0], dt_string[2:8]), '%m/%d/%Y')
            except:
                print('all date conversions failed on value {}'.format(dt_string))
                pass
        return fixed_dt
    
def df_make_rename_drop(data, col_dict=None, cols_to_drop=None, rows_to_drop=None):
    try:
        df = pd.DataFrame(data).rename(columns=col_dict)
    except Exception as e:
        print('conversion of object {} to pd.Dataframe failed'.format(data))
        print('with exception {}'.format(e))
        return None
    if col_dict:
        try:
            df.rename(columns=col_dict)
        except Exception as e:
            print('column rename failed for DataFrame {}'.format(df))
            print('with exception {}'.format(e))
    if cols_to_drop:
        try:
            df = df.drop(cols_to_drop, axis = 1)
        except KeyError: 
            print('the columns to drop were not present in {}'.format(df))
    if rows_to_drop:
        try:
            df = df.drop(rows_to_drop, axis = 0)
        except KeyError: 
            print('the rows to drop were not present in {}'.format(df))
    return df

def to_sql_replace(sa_engine, tbl_name, data_dir, filename, filetype, delimiter=','):
    if filetype == 'csv':
        try:
            data_df = pd.read_csv('{}{}'.format(data_dir, filename), delimiter=delimiter)
            data_df.to_sql(tbl_name, sa_engine, if_exists='replace', index=False)
        except Exception as e: 
            print('send to sql failed with exception {}'.format, e)
        finally:
            return
    if filetype == 'excel':
        try:
            data_df = pd.read_excel('{}{}'.format(data_dir, filename))
            data_df.to_sql(tbl_name, sa_engine, if_exists='replace', index=False)
        except Exception as e:
            print('send to sql failed with exception {}'.format, e)
        finally:
            return
    return
    