


import pandas as pd 
import xlsxwriter
from loguru import logger
from typing import Dict # Pour typer le dictionnaire


def excel_repporting(file: str, onglets : Dict[str, pd.DataFrame], valeur_red_format,  min_orange_format, max_orange_format, grenn_format_marge):
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        logger.info('Ouverture du Contexte manager')
        workbook = writer.book
        logger.info('Création du Fichier Excel')
        base = {
            'align' : 'center',
            'valign' : 'center',
            'border' : 1,
        }
        base_format = workbook.add_format(base)
        header_format = workbook.add_format(
            {
                **base,
                'bold' : True,
                'italic' : True,
                'bg_color' : '#4F81BD',
                'font_color' : 'white'
            }
        )
        money_format = workbook.add_format({**base, 'num_format' : '#,##0 €'})
        marge_format = workbook.add_format({**base, 'num_format' : '0 %'})
        time_format = workbook.add_format({**base, 'num_format' : 'hh"H":mm"M":ss"S"'})
        red_format = workbook.add_format({**base, 'bg_color' : '#FFC7CE'})
        orange_format = workbook.add_format({**base, 'bg_color' : '#FFEB9C'})
        green_format = workbook.add_format({**base, 'bg_color' : '#13FF3A'})
        for name, data in onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            logger.info(f'Création de la feuille {name}')
            worksheet = writer.sheets[name]
            for column_numb, value in enumerate(data.columns):
                worksheet.write(0, column_numb, value, header_format)
            logger.info(f'Application des formats sur les headers pour la feuille {name}')
            worksheet.freeze_panes(1, 0)
            logger.info(f'Fixation du header pour la feuille {name}')
            worksheet.autofilter(0, 0, len(data), len(data.columns) - 1)
            logger.info(f'Application du filtrage automatique sur les headers pour la feuille {name}')
            column_money = ['Revenue', 'Cout', 'Montant_bonus', 'Profit', 'Prix_Unitaire', 'Coût_Unitaire']
            column_marge = ['Bonus_%', 'Marge', 'Marge_totaux']
            for i, column in enumerate(data.columns):
                column_width = max(data[column].astype(str).str.len().max() , len(column)) + 3
                if column in column_marge:
                    worksheet.set_column(i, i, column_width, marge_format)
                elif column in column_money:
                    worksheet.set_column(i, i, column_width, money_format)
                #elif column == "Heure_d'achat":
                    #worksheet.set_column(i, i, column_width, time_format)
                else:
                    worksheet.set_column(i, i, column_width, base_format)

                logger.info(f"Application de l'ajoutement automatique et des différents formatages sur la colonne {column} pour la feuille {name}")


                if name == 'Données Brutes Néttoyes' or 'Données Propre Complét':
                    if column == "Heure_d'achat":
                        worksheet.set_column(i, i, column_width, time_format)
                    if 'Profit' in data.columns:
                        profit_column = data.columns.get_loc('Profit')
                        worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                            'type' : 'cell',
                            'criteria' : '<',
                            'value' : valeur_red_format,
                            'format' : red_format
                        })

                        worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                            'type' : 'cell',
                            'criteria' : 'between',
                            'minimum' : min_orange_format,
                            'maximum' : max_orange_format,
                            'format' : orange_format
                        })

                    if 'Marge' in data.columns:
                        marge_column = data.columns.get_loc('Marge')
                        worksheet.conditional_format(1, marge_column, len(data), marge_column, {
                        'type' : 'cell',
                        'criteria' : '>',
                        'value' : grenn_format_marge,
                        'format' : green_format
                        })

                    logger.info(f"Applcation des conditional format de base pour la feuille {name}")
                adaptated_sheet = ['Données Par Produit', 'Données Par Région' , 'Données Par Type_Client' , 'Données Par Mois' , 'Données Par Jour']
                if name in adaptated_sheet:
                    if 'Profit' in data.columns:
                        profit_column = data.columns.get_loc('Profit')
                        worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                            'type' : 'cell',
                            'criteria' : '<',
                            'value' : 0,#100000,
                            'format' : red_format
                        })

                        worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                            'type' : 'cell',
                            'criteria' : 'between',
                            'minimum' : 0,#100000,
                            'maximum' : 30000,#1000000,
                            'format' : orange_format
                        })

                        worksheet.conditional_format(1, profit_column, len(data), profit_column, {
                            'type' : 'cell',
                            'criteria' : '>',
                            'value' : 30000,#100000,
                            'format' : green_format
                        })

                    if 'Marge_totaux' in data.columns:
                        marge_totaux_column = data.columns.get_loc('Marge_totaux')
                        worksheet.conditional_format(1, marge_totaux_column, len(data), marge_totaux_column, {
                            'type' : 'cell',
                            'criteria' : '<',
                            'value' : 0,
                            'format' : red_format
                        })

                        worksheet.conditional_format(1, marge_totaux_column, len(data), marge_totaux_column, {
                            'type' : 'cell',
                            'criteria' : 'between',
                            'minimum' : 0,
                            'maximum' : 0.25,
                            'format' : orange_format
                        })

                        worksheet.conditional_format(1, marge_totaux_column, len(data), marge_totaux_column, {
                            'type' : 'cell',
                            'criteria' : '>',
                            'value' : 0.25,
                            'format' : green_format
                        })
                    logger.info(f"Application des conditional format spécifique aux analyses pour la feuille {name}")

                if name == 'Données Par Produit':
                    logger.info(f"Début de la création du graphique pour la feuille {name}")
                    chart_col = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    produit_column = data.columns.get_loc('Produit')
                    revenue_column = data.columns.get_loc('Revenue')
                    profit_column = data.columns.get_loc('Profit')
            
                    chart_col.add_series(
                        {
                            'name' : 'Revenue',
                            'categories' : [name, 1, produit_column, len(data), produit_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column]
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Profit',
                            'categories' : [name, 1, produit_column, len(data), produit_column],
                            'values' : [name, 1, profit_column, len(data), profit_column],
                            'y2_axis' : True
                        }
                    )
                    chart_col.combine(chart_line)
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)
                    logger.info(f"Graphique crée avec succée pour la feuille {name}")

                if name == 'Données Par Région':
                    logger.info(f"Début de la création du graphique pour la feuille {name}")

                    chart_pie = workbook.add_chart({'type' : 'pie'})
                    region_column = data.columns.get_loc('Region')
                    revenue_column = data.columns.get_loc('Revenue')

                    chart_pie.add_series(
                        {
                            'name' : 'Revenue',
                            'categories' : [name, 1, region_column, len(data), region_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column],
                            'data_labels' : {'percentage' : True,'category' : True,'position' : 'outside_end'}
                        }                
                    )
                    chart_pie.set_legend({'position' : 'none'})
                    chart_pie.set_title({'name' : 'Répartition du Revenue Par Région'})
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_pie)
                    logger.info(f"Graphique crée avec succée pour la feuille {name}")

                if name == 'Données Par Mois':
                    logger.info(f"Début de la création du graphique pour la feuille {name}")
                    chart_line = workbook.add_chart({'type' : 'column'})
                    chart_line2 = workbook.add_chart({'type' : 'line'})
                    mois_column = data.columns.get_loc('Mois')
                    revenue_column = data.columns.get_loc('Revenue')
                    profit_column = data.columns.get_loc('Profit')

                    chart_line.add_series(
                        {
                            'name' : 'Revenue',
                            'categories' : [name, 1, mois_column, len(data), mois_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column]
                        }
                    )
            
                    chart_line2.add_series(
                        {
                            'name' : 'Profit',
                            'categories' : [name, 1, mois_column, len(data), mois_column],
                            'values' : [name, 1, profit_column, len(data), profit_column]
                        }
                    )

                    chart_line.combine(chart_line2)
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_line)
                    logger.info(f"Graphique crée avec succée pour la feuille {name}")

                if name == 'Données Par Jour':
                    logger.info(f"Début de la création du graphique pour la feuille {name}")
                    chart_col = workbook.add_chart({'type' : 'column'})
                    #chart_col2 = workbook.add_chart({'type' : 'column'})
                    chart_line = workbook.add_chart({'type' : 'line'})
                    jour_column = data.columns.get_loc('jour_semaine')
                    revenue_column = data.columns.get_loc('Revenue')
                    profit_column = data.columns.get_loc('Profit')
                    marge_column = data.columns.get_loc('Marge_totaux')

                    chart_col.add_series(
                        {
                            'name' : 'Revenue',
                            'categories' : [name, 1, jour_column, len(data), jour_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column]
                        }
                    )
            
                    chart_col.add_series(
                        {
                            'name' : 'Profit',
                            'categories' : [name, 1, jour_column, len(data), jour_column],
                            'values' : [name, 1, profit_column, len(data), profit_column]
                        }
                    )

                    chart_line.add_series(
                        {
                            'name' : 'Marge_Totaux',
                            'categories' : [name, 1, jour_column, len(data), jour_column],
                            'values' : [name, 1, marge_column, len(data), marge_column],
                            'y2_axis' : True
                        }
                    )

                    chart_col.combine(chart_line)
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_col)
                    logger.info(f"Graphique crée avec succée pour la feuille {name}")

                if name == 'Données Par Type_Client':
                    logger.info(f"Début de la création du graphique pour la feuille {name}")
                    chart_pie = workbook.add_chart({'type' : 'pie'})
                    type_column = data.columns.get_loc('Type_Client')
                    revenue_column = data.columns.get_loc('Revenue')

                    chart_pie.add_series(
                        {
                            'name' : 'Revenue',
                            'categories' : [name, 1, type_column, len(data), type_column],
                            'values' : [name, 1, revenue_column, len(data), revenue_column],
                            'data_labels' : {'percentage' : True,'category' : True,'position' : 'outside_end'}
                        }                
                    )
                    chart_pie.set_legend({'position' : 'none'})
                    chart_pie.set_title({'name' : 'Répartition du Revenue Type De Client'})
                    worksheet.insert_chart(1, data.shape[1] + 1, chart_pie)
                    logger.info(f"Graphique crée avec succée pour la feuille {name}")
        logger.success(f"Feuille Excel de Repporting {name} crée avec succée")

    logger.success(f"Fichier Excel de Repporting {file.name} a étais crée avec succée")





    print(f"Fichier {file.name} crée avec succée")