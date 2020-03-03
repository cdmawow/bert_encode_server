nohup python ../feature_server.py \
  -model_dir ~/pretrained_lm/bert_wwm_chinese/ \
  -ckpt_name bert_model.ckpt \
  -config_name bert_config.json \
  -priority_batch_size 2 \
  -num_worker 1 \
  -port 2701 \
  -port_out 2702 \
  -http_port 2706 \
  -http_max_connect 40 \
  -max_seq_len 35 \
  -no_special_token \
  -cpu >> sent_logs.out &
#  -albert \