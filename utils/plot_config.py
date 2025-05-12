import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
import locale

def configure_plot_style():
    """Configura o estilo padrão para todos os gráficos"""
    sns.set()
    plt.style.use('seaborn-v0_8-notebook')
    rcParams['figure.figsize'] = (6, 4)
    rcParams['figure.titlesize'] = 14
    rcParams['font.size'] = 15
    
    # Esquema de cores personalizado
    global my_colors
    my_colors = ['#008E5A', '#00A868', '#0FCC7D', '#B5B0AE', '#D0D0D0', '#EFF4F8']
    sns.set_palette(my_colors)



class PlotUtils:
    """Classe utilitária para criação de gráficos"""

    @staticmethod
    def _save_plot(filename=None, dpi=300, transparent=False):
        """
        Salva o gráfico atual em arquivo, se filename for fornecido
        """
        if filename:
            plt.savefig(
                filename,
                dpi=dpi,
                transparent=transparent,
                bbox_inches='tight',
                pad_inches=0.3)
    
    
    @staticmethod
    def pie_chart(data, x=None, y=None, title=None, explode=None, colors=None, 
                 autopct_format='both', startangle=90, textprops=None, title_fontsize=12,
                 value_fontsize=12, figsize=(6, 4), locale_format=True, save_to=None, 
                 dpi=300, transparent=False):
        """
        Cria um gráfico de pizza
        
        """
        # Extrair os dados conforme o tipo de entrada
        if isinstance(data, pd.DataFrame):
            labels = data[x] if x else data.index
            values = data[y] if y else data.iloc[:, 0]
        else:  # Series
            labels = data.index
            values = data.values
        
        total = sum(values)
        porcentagens = [v/total * 100 for v in values]
        
        # Configurações padrão
        if explode is None:
            explode = [0.02] * len(values)
        
        if colors is None:
            colors = ['#1F6FF0', '#0eafaa']
        
        if textprops is None:
            textprops = {'fontsize': 10}
        
        # Criar figura
        fig, ax = plt.subplots(figsize=figsize)
        
        # Função de formatação do autopct
        def autopct_func(p):
            if autopct_format == 'percent':
                return f'{p:.1f}%'
            elif autopct_format == 'value':
                if locale_format:
                    valor = p * total / 100
                    valor_fmt = locale.format_string('%d', round(valor), grouping=True)
                    return f"R${valor_fmt}"
                return f"R${p * total / 100:,.0f}"
            else:  # both
                if locale_format:
                    valor = p * total / 100
                    valor_fmt = locale.format_string('%d', round(valor), grouping=True)
                    return f"{p:.1f}%\n(R${valor_fmt})"
                return f"{p:.1f}%\n(R${p * total / 100:,.0f})"
        
        # Plotar o gráfico
        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            autopct=autopct_func,
            startangle=startangle,
            colors=colors,
            explode=explode,
            textprops=textprops
        )
        
        # Ajustar fontes dos valores
        for autotext in autotexts:
            autotext.set_fontsize(value_fontsize)
        
        # Adicionar título
        if title:
            ax.set_title(title, pad=20, fontsize=title_fontsize)
        
        plt.tight_layout()
        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()
    


    
    @staticmethod
    def box_plot(data, x, y, title, xlabel=None, ylabel=None, rotation=0, save_to=None, dpi=300, transparent=False):
        """
        Cria um boxplot

        """
        sns.boxplot(data=data, x=x, y=y, color=my_colors[2])
        plt.title(title, fontweight='bold')
        
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.xticks(rotation=rotation)

        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()




    @staticmethod
    def bar_plot(data, x, y=None, title=None, xlabel=None, ylabel=None, 
                 rotation=45, order=None, color_index=2, figsize=(6, 4),
                 save_to=None, dpi=300, transparent=False):
        """
        Cria um gráfico de barras verticais ordenado
        
        """
        plt.figure(figsize=figsize)
        
        if y:
            sns.barplot(data=data, x=x, y=y, order=order, color=my_colors[color_index])
        else:
            sns.countplot(data=data, x=x, order=order, color=my_colors[color_index])
        
        plt.title(title, fontweight='bold')
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel if ylabel else 'Contagem' if not y else y)
        plt.xticks(rotation=rotation)
        plt.tight_layout()
        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()
    
    
    
    
    @staticmethod
    def hist_plot(data, x, title=None, xlabel=None, ylabel='Contagem', 
                  bins='auto', color_index=0, shrink=0.8, rotation=0, color='#002768',
                  save_to=None, dpi=300, transparent=False):
        """
        Cria um histograma
        
        """
        sns.histplot(data=data, x=x, bins=bins, shrink=shrink, 
                    color=color)
        plt.title(title if title else f'Distribuição de {x}', fontweight='bold')
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel)
        plt.xticks(rotation=rotation)
        plt.tight_layout()
        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()
    
    
    
    
    @staticmethod
    def line_plot(data, x, y, title=None, xlabel=None, ylabel=None, 
                  color_index=0, marker='o', linewidth=2.5, grid=True,
                  sort_by_y=False, rotation=0, fontsize=10, save_to=None,
                  dpi=300, transparent=False):
        """
        Cria um gráfico de linhas

        """
        # Ordena os dados se necessário
        if sort_by_y:
            data = data.sort_values(by=y, ascending=False).copy()  # `.copy()` evita warnings

        sns.lineplot(data=data, x=x, y=y, marker=marker, 
                    color=my_colors[color_index], linewidth=linewidth)
        
        plt.title(title if title else f'{y} por {x}', fontweight='bold')
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel if ylabel else y)
        plt.xticks(rotation=rotation, fontsize=fontsize)
        
        if grid:
            plt.grid(axis='y', linestyle='--', alpha=0.3)
        
        plt.tight_layout()
        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()
    
    
    
    
    @staticmethod
    def point_plot(data, x, y, title=None, xlabel=None, ylabel=None, 
                color_index=0, marker='o', linewidth=2.5, grid=True,
                sort_by_y=False, rotation=0, save_to=None, dpi=300, transparent=False):
        """
        Cria um gráfico de pontos
        """
        # Ordena os dados se necessário
        data = data.sort_values(by=y, ascending=False) if sort_by_y else data
      
        # Usar sns.pointplot ou plt.plot para manter a ordem
        sns.pointplot(data=data, x=x, y=y, order=data[x] if sort_by_y else None,
                    color=my_colors[color_index], linestyles='-', markers=marker)
        
        plt.title(title if title else f'{y} por {x}', fontweight='bold')
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel if ylabel else y)
        plt.xticks(rotation=rotation)
        
        if grid:
            plt.grid(axis='y', linestyle='--', alpha=0.3)
        
        plt.tight_layout()
        PlotUtils._save_plot(save_to, dpi, transparent)
        plt.show()