import xml_to_csv
import struct

def main():
    # image_path = os.path.join(os.getcwd(), 'annotations')
    image_path = r'E:\test\datas\xml'
    xml_df = xml_to_csv.xml_to_csv(image_path)
    xml_df.to_csv(path_or_buf=r'E:\test\datas\person_labels.csv', index=None)
    print('Successfully converted xml to csv.')
if __name__ == '__main__':
    main()