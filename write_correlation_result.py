from correlation import correlation, re_correlation, read_data
import warnings
import math

warnings.filterwarnings("ignore")

arg_path = r'C:\Users\Administrator\Desktop\zzmpr\ARG.xlsx'
mge_path = r'C:\Users\Administrator\Desktop\zzmpr\MGE.xlsx'
phylum_path = r'C:\Users\Administrator\Desktop\zzmpr\Phylum.xlsx'
env_path = r'C:\Users\Administrator\Desktop\zzmpr\environment.xlsx'


# def write_content(file, q_mge_arg, q_phy_arg, q_env_arg, h_mge_arg, h_phy_arg, h_env_arg):
#     with open(file, 'w+', encoding="gbk") as f:
#         q_one = math.ceil(q_mge_arg + q_env_arg + q_phy_arg)
#         dfq_content = """"""
#         dfq_content += "堆肥前 MGE --> ARG: %.4f\n" % (float(q_mge_arg) / q_one)
#
#         dfq_content += "堆肥前 phylum --> ARG: %.4f\n" % (float(q_phy_arg) / q_one)
#         dfq_content += "堆肥前 environment --> ARG: %.4f\n" % (float(q_env_arg) / q_one)
#         dfq_content += "堆肥前 unexplained --> ARG: %.4f\n" % (
#                 (q_one - float((q_mge_arg + q_env_arg + q_phy_arg))) / q_one)
#         f.write(dfq_content)
#
#         h_one = math.ceil(h_mge_arg + h_env_arg + h_phy_arg)
#         dfh_content = """\n"""
#         dfh_content += "堆肥后 MGE --> ARG: %.4f\n" % (float(h_mge_arg) / h_one)
#         dfh_content += "堆肥后 phylum --> ARG: %.4f\n" % (float(h_phy_arg) / h_one)
#         dfh_content += "堆肥后 environment --> ARG: %.4f\n" % (float(h_env_arg) / h_one)
#         dfh_content += "堆肥后 unexplained --> ARG: %.4f\n" % (
#                 (h_one - float((h_mge_arg + h_env_arg + h_phy_arg))) / h_one)
#         f.write(dfh_content)


# pearson, p

def write_content(file, q_mge_arg, q_phy_arg, q_env_arg, h_mge_arg, h_phy_arg, h_env_arg):
    with open(file, 'w+', encoding="gbk") as f:
        content = """"""
        all_1 = q_mge_arg + q_phy_arg + q_env_arg
        mge_q = (float(q_mge_arg) / all_1)

        phy_q = (float(q_phy_arg) / all_1)
        env_q = (float(q_env_arg) / all_1)


        all_2 = h_mge_arg + h_phy_arg + h_env_arg

        mge_h = (float(h_mge_arg) / all_2)
        phy_h = (float(h_phy_arg) / all_2)
        env_h = (float(h_env_arg) / all_2)


        all_4 = abs(phy_h-phy_q) + (abs(env_h-env_q)) + (abs(mge_h-mge_q))
        all_3 = (int(all_4 * 10) + 1)/10
        content += "phylum: %.4f\n" % (abs(phy_h-phy_q) /all_3)
        content += "env: %.4f\n" % ((abs(env_h-env_q))/all_3)
        content += "mge: %.4f\n" % ((abs(mge_h-mge_q))/all_3)
        content += "unexplained: %.4f\n" % abs((all_3-all_4)/all_3)
        f.write(content)
        

dfq_mge_arg1 = re_correlation(read_data(mge_path, 0), read_data(arg_path, 0))
dfq_phylum_arg1 = re_correlation(read_data(phylum_path, 0), read_data(arg_path, 0))
dfq_env_arg1 = re_correlation(read_data(env_path, 0), read_data(arg_path, 0))
dfh_mge_arg1 = re_correlation(read_data(mge_path, 1), read_data(arg_path, 1))
dfh_phylum_arg1 = re_correlation(read_data(phylum_path, 1), read_data(arg_path, 1))
dfh_env_arg1 = re_correlation(read_data(env_path, 1), read_data(arg_path, 1))

dfq_mge_arg2 = re_correlation(read_data(mge_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfq_phylum_arg2 = re_correlation(read_data(phylum_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfq_env_arg2 = re_correlation(read_data(env_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfh_mge_arg2 = re_correlation(read_data(mge_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)
dfh_phylum_arg2 = re_correlation(read_data(phylum_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)
dfh_env_arg2 = re_correlation(read_data(env_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)

# spearman, p

dfq_mge_arg3 = re_correlation(read_data(mge_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=0)
dfq_phylum_arg3 = re_correlation(read_data(phylum_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=0)
dfq_env_arg3 = re_correlation(read_data(env_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=0)
dfh_mge_arg3 = re_correlation(read_data(mge_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=0)
dfh_phylum_arg3 = re_correlation(read_data(phylum_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=0)
dfh_env_arg3 = re_correlation(read_data(env_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=0)

# spearman, r

dfq_mge_arg4 = re_correlation(read_data(mge_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=1)
dfq_phylum_arg4 = re_correlation(read_data(phylum_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=1)
dfq_env_arg4 = re_correlation(read_data(env_path, 0), read_data(arg_path, 0), correlation_type=2, s_index=1)
dfh_mge_arg4 = re_correlation(read_data(mge_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=1)
dfh_phylum_arg4 = re_correlation(read_data(phylum_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=1)
dfh_env_arg4 = re_correlation(read_data(env_path, 1), read_data(arg_path, 1), correlation_type=2, s_index=1)



dfq_mge_arg5 = correlation(read_data(mge_path, 0), read_data(arg_path, 0))
dfq_phylum_arg5 = correlation(read_data(phylum_path, 0), read_data(arg_path, 0))
dfq_env_arg5 = correlation(read_data(env_path, 0), read_data(arg_path, 0))
dfh_mge_arg5 = correlation(read_data(mge_path, 1), read_data(arg_path, 1))
dfh_phylum_arg5 = correlation(read_data(phylum_path, 1), read_data(arg_path, 1))
dfh_env_arg5 = correlation(read_data(env_path, 1), read_data(arg_path, 1))

dfq_mge_arg6 = correlation(read_data(mge_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfq_phylum_arg6 = correlation(read_data(phylum_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfq_env_arg6 = correlation(read_data(env_path, 0), read_data(arg_path, 0), correlation_type=1, p_index=1)
dfh_mge_arg6 = correlation(read_data(mge_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)
dfh_phylum_arg6 = correlation(read_data(phylum_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)
dfh_env_arg6 = correlation(read_data(env_path, 1), read_data(arg_path, 1), correlation_type=1, p_index=1)

write_content("c1.txt", dfq_mge_arg1, dfq_phylum_arg1, dfq_env_arg1, dfh_mge_arg1, dfh_phylum_arg1, dfh_env_arg1)
write_content("c2.txt", dfq_mge_arg2, dfq_phylum_arg2, dfq_env_arg2, dfh_mge_arg2, dfh_phylum_arg2, dfh_env_arg2)
write_content("c3.txt", dfq_mge_arg3, dfq_phylum_arg3, dfq_env_arg3, dfh_mge_arg3, dfh_phylum_arg3,
              dfh_env_arg3)
write_content("c4.txt", dfq_mge_arg4, dfq_phylum_arg4, dfq_env_arg4, dfh_mge_arg4, dfh_phylum_arg4,
              dfh_env_arg4)
write_content("c5.txt", dfq_mge_arg5, dfq_phylum_arg5, dfq_env_arg5, dfh_mge_arg5, dfh_phylum_arg5,
              dfh_env_arg5)
write_content("c6.txt", dfq_mge_arg6, dfq_phylum_arg6, dfq_env_arg6, dfh_mge_arg6, dfh_phylum_arg6,
              dfh_env_arg6)

# change_mge_arg1 = abs(dfq_mge_arg1 - dfh_mge_arg1)
# change_phylum_arg1 = abs(dfq_phylum_arg1 - dfh_phylum_arg1)
# change_env_arg1 = abs(dfq_env_arg1 - dfh_env_arg1)
# r1 = math.ceil(change_phylum_arg1 + change_mge_arg1 + change_env_arg1)
# with open("change1.txt", 'w') as f1:
#     content1 = """"""
#     content1 += "phylum: %.4f\n" % (change_phylum_arg1 / r1)
#     content1 += "env: %.4f\n" % (change_env_arg1 / r1)
#     content1 += "mge: %.4f\n" % (change_mge_arg1 / r1)
#     content1 += "unexplained: %.4f\n" % ((r1 - (change_phylum_arg1 + change_env_arg1 + change_mge_arg1)) / r1)
#     f1.write(content1)
#
# change_mge_arg2 = abs(dfq_mge_arg2 - dfh_mge_arg2)
# change_phylum_arg2 = abs(dfq_phylum_arg2 - dfh_phylum_arg2)
# change_env_arg2 = abs(dfq_env_arg2 - dfh_env_arg2)
# r2 = math.ceil(change_phylum_arg2 + change_mge_arg2 + change_env_arg2)
# with open("change2.txt", 'w') as f2:
#     content2 = """"""
#     content2 += "phylum: %.4f\n" % (change_phylum_arg2 / r2)
#     content2 += "env: %.4f\n" % (change_env_arg2 / r2)
#     content2 += "mge: %.4f\n" % (change_mge_arg2 / r2)
#     content2 += "unexplained: %.4f\n" % ((r2 - (change_phylum_arg2 + change_env_arg2 + change_mge_arg2)) / r2)
#     f2.write(content2)
#
# change_mge_arg3 = abs(dfq_mge_arg3 - dfh_mge_arg3)
# change_phylum_arg3 = abs(dfq_phylum_arg3 - dfh_phylum_arg3)
# change_env_arg3 = abs(dfq_env_arg3 - dfh_env_arg3)
# r3 = math.ceil(change_phylum_arg3 + change_mge_arg3 + change_env_arg3)
# with open("change3.txt", 'w') as f3:
#     content3 = """"""
#     content3 += "phylum: %.4f\n" % (change_phylum_arg3 / r3)
#     content3 += "env: %.4f\n" % (change_env_arg3 / r3)
#     content3 += "mge: %.4f\n" % (change_mge_arg3 / r3)
#     content3 += "unexplained: %.4f\n" % ((r3 - (change_phylum_arg3 + change_env_arg3 + change_mge_arg3)) / r3)
#     f3.write(content3)
#
# change_mge_arg4 = abs(dfq_mge_arg4 - dfh_mge_arg4)
# change_phylum_arg4 = abs(dfq_phylum_arg4 - dfh_phylum_arg4)
# change_env_arg4 = abs(dfq_env_arg4 - dfh_env_arg4)
# r4 = math.ceil(change_phylum_arg4 + change_mge_arg4 + change_env_arg4)
# with open("change4.txt", 'w') as f4:
#     content4 = """"""
#     content4 += "phylum: %.4f\n" % (change_phylum_arg4 / r4)
#     content4 += "env: %.4f\n" % (change_env_arg4 / r4)
#     content4 += "mge: %.4f" % (change_mge_arg4 / r4)
#     content4 += "unexplained: %.4f\n" % ((r4 - (change_phylum_arg4 + change_env_arg4 + change_mge_arg4)) / r4)
#     f4.write(content4)
#
# change_mge_arg5 = abs(dfq_mge_arg5 - dfh_mge_arg5)
# change_phylum_arg5 = abs(dfq_phylum_arg5 - dfh_phylum_arg5)
# change_env_arg5 = abs(dfq_env_arg5 - dfh_env_arg5)
#
# r5 = math.ceil(change_phylum_arg5 + change_mge_arg5 + change_env_arg5)
# with open("change5.txt", 'w') as f5:
#     content5 = """"""
#     content5 += "phylum: %.4f\n" % (change_phylum_arg5 / r5)
#     content5 += "env: %.4f\n" % (change_env_arg5 / r5)
#     content5 += "mge: %.4f\n" % (change_mge_arg5 / r5)
#     content5 += "unexplained: %.4f\n" % ((r5 - (change_phylum_arg5 + change_env_arg5 + change_mge_arg5)) / r5)
#     f5.write(content5)
#
# change_mge_arg6 = abs(dfq_mge_arg6 - dfh_mge_arg6)
# change_phylum_arg6 = abs(dfq_phylum_arg6 - dfh_phylum_arg6)
# change_env_arg6 = abs(dfq_env_arg6 - dfh_env_arg6)
#
# r6 = math.ceil(change_phylum_arg6 + change_mge_arg6 + change_env_arg6)
# with open("change6.txt", 'w') as f6:
#     content6 = """"""
#     content6 += "phylum: %.4f\n" % (change_phylum_arg6 / r6)
#     content6 += "env: %.4f\n" % (change_env_arg6 / r6)
#     content6 += "mge: %.4f\n" % (change_mge_arg6 / r6)
#     content6 += "unexplained: %.4f\n" % ((r6 - (change_phylum_arg6 + change_env_arg6 + change_mge_arg6)) / r6)
#     f6.write(content6)
