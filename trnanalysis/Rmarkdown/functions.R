setClass(Class="filter_genes_return",
         representation(
           res="data.frame",
           sig="data.frame"
         )
)

filter_genes <- function(result, name){
  
  test <- as.data.frame(result)
  test["name"] <- rownames(test) 
  res <- test %>% 
    dplyr::select(name, log2FoldChange,baseMean, padj) %>% 
    na.omit()
  
  sig <- res %>% 
    filter(log2FoldChange > 1 | log2FoldChange < -1) %>% 
    filter(padj < 0.05)
  dir.create(file.path("results"), showWarnings = FALSE)
  sig_name = paste("results/", name,"_sig.csv", sep="")
  sig_name_tsv = paste("results/", name,"_sig.tsv", sep="")
  res_name = paste("results/",name,"_res.csv", sep="")
  res_name_tsv = paste("results/", name,"_res.tsv", sep="")
  write_csv(sig, sig_name)
  write_csv(res, res_name)
  write_tsv(sig, sig_name_tsv)
  write_tsv(res, res_name_tsv)
  return(new("filter_genes_return",
             res=res,
             sig=sig))
}


filter_genes_single <- function(result, name){
  
  test <- as.data.frame(result)
  
  data <- as.vector(rownames(test))
  annots <-  AnnotationDbi::select(org.Hs.eg.db, keys=data,
                                   columns="SYMBOL", keytype = "ENSEMBL")
  
  result <- merge(test, annots, by.x="row.names", by.y="ENSEMBL")
  res <- result %>% 
    dplyr::select(log2FoldChange, SYMBOL, baseMean, padj, Row.names) %>% 
    na.omit()
  
  sig <- res %>% 
    filter(log2FoldChange > 2 | log2FoldChange < -2)
  
  sig_name = paste("results/", name,"_sig.csv", sep="")
  sig_name_tsv = paste("results/", name,"_sig.tsv", sep="")
  res_name = paste("results/",name,"_res.csv", sep="")
  res_name_tsv = paste("results/", name,"_res.tsv", sep="")
  write_csv(sig, sig_name)
  write_csv(res, res_name)
  write_tsv(sig, sig_name_tsv)
  write_tsv(res, res_name_tsv)
  return(list("sig"= sig, "res"= res))
}

run_deseq2_full <- function(df_mRNA, meta_data, model){
  
  
  dds<- DESeqDataSetFromMatrix(countData=df_mRNA,
                               colData=meta_data,
                               design=as.formula(model)) 
  
  keep <- rowSums(counts(dds)) >= 10
  dds <- dds[keep,]
  
  dds <- DESeq(dds, parallel=TRUE)
  
  return(dds)
}





setClass(Class="DESeq2_return",
         representation(
           res="DESeqResults",
           dds="DESeqDataSet"
         )
)


run_deseq2 <- function(df_mRNA, meta_data, control="untreated", test="treated", value, model){
  
  df_mRNA = df_mRNA[,rownames(meta_data)]
  
  
  dds<- DESeqDataSetFromMatrix(countData=df_mRNA,
                               colData=meta_data,
                               design=as.formula(model))
  
  keep <- rowSums(counts(dds)) >= 10
  dds <- dds[keep,]
  
  dds <- DESeq(dds)
  
  res <- results(dds, contrast = c(value, test,control))
  
  return(new("DESeq2_return",
             res=res,
             dds=dds))
}

setClass(Class="DESeq2_lrt_return",
         representation(
           res="DESeqResults",
           dds="DESeqDataSet"
         )
)


run_deseq2_lrt <- function(df_mRNA, meta_data, control="untreated", test="treated", value, model,
                           reduced){
  
  df_mRNA = df_mRNA[,rownames(meta_data)]
  
  
  dds<- DESeqDataSetFromMatrix(countData=df_mRNA,
                               colData=meta_data,
                               design=as.formula(model))
  
  keep <- rowSums(counts(dds)) >= 10
  dds <- dds[keep,]
  
  dds <- DESeq(dds, test="LRT", reduced =as.formula(reduced))
  
  res <- results(dds, contrast = c(value, test,control))
  
  return(new("DESeq2_lrt_return",
             res=res,
             dds=dds))
}



plot_volcano <- function(res){
  
  result <- as.data.frame(res)
  
  res <- result %>% 
    dplyr::select(log2FoldChange, baseMean, padj) %>% 
    na.omit()
  res['plot'] <- rownames(res)
  
  mutateddf <- mutate(res, sig=ifelse(res$padj<0.01, "padj<0.01", "Not Sig")) #Will have different colors depending on significance
  input <- cbind(gene=rownames(mutateddf), mutateddf )
  input <- input %>% 
    arrange(input$padj)
  
  symbol_data <- head(input, 30)
  
  #convert the rownames to a column
  volc = ggplot(input, aes(log2FoldChange, -log10(padj))) + #volcanoplot with log2Foldchange versus pvalue
    geom_point(aes(col=sig)) + #add points colored by significance
    geom_point(data=symbol_data, aes(log2FoldChange, -log10(padj)), colour="red") +
    ggtitle("Volcano") #e.g. 'Volcanoplot DESeq2'
  
  
  #setEPS()
  #postscript("MUG_volcano.eps")
  volcano <- volc+geom_text_repel(data=symbol_data, aes(label=`plot`)) + scale_colour_Publication() + theme_bw()#adding text for the genes
  return(volcano)
}