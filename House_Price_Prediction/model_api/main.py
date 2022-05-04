from unittest import result
import pandas as pd
import numpy as np
import pickle
from flask import Flask,request
# from requests import post, request

app=Flask(__name__)

model=pickle.load(open(r"E:\10.python\project\project2\model_api\price.pkl","rb"))
columns=pickle.load(open(r"E:\10.python\project\project2\model_api\Columns.pkl","rb"))

@app.route("/hhpPrediction")
def hhpPrediction():
    data=request.form
    vector=np.zeros(209)
    print(vector)
    vector[0]=data["MSSubClass"]
    vector[1]=data["LotFrontage"]
    vector[2]=data["LotArea"]
    LotShape=data["LotShape"]
    OverallQual=data["OverallQual"]
    OverallCond=data["OverallCond"]
    vector[6]=data["YearBuilt"]
    vector[7]=data["YearRemodAdd"]
    vector[8]=data["MasVnrArea"]
    ExterQual=data["ExterQual"]
    ExterCond=data["ExterCond"]
    BsmtQual=data["BsmtQual"]
    BsmtCond=data["BsmtCond"]
    BsmtExposure=data["BsmtExposure"]
    BsmtFinType1=data["BsmtFinType1"]  #Good Living Quarters
    vector[15]=data["BsmtFinSF1"]
    BsmtFinType2=data["BsmtFinType2"]
    vector[17]=data["BsmtFinSF2"]
    vector[18]=data["BsmtUnfSF"]
    vector[19]=data["TotalBsmtSF"]
    HeatingQC=data["HeatingQC"]
    vector[21]=data["First_Floor_square_feet"]
    vector[22]=data["Second_floor_square_feet"]
    vector[23]=data["Low_quality_finished_square_feet"]
    vector[24]=data["living_area_square_feet"]
    vector[25]=data['Basement_full_bathrooms']
    vector[26]=data["Basement_half_bathrooms"]
    vector[27]=data["Full_bathrooms"]
    vector[28]=data["Half_baths"]
    vector[29]=data["Bedrooms"]
    vector[30]=data["Kitchens"]
    KitchenQual=data["Kitchen_quality"]
    vector[32]=data["Total_rooms"]
    vector[33]=data["Fireplaces"]
    FireplaceQu=data["Fireplace_quality"]    
    vector[35]=data['Year_garage_was_built']
    GarageFinish=data["Interior_finish_of_the_garage"]
    vector[37]=data["Size_of_garage_in_car_capacity"]
    vector[38]=data["Size_of_garage_in_square_feet"]
    GarageQual=data["Garage_quality"]
    GarageCond=data["Garage_condition"]
    vector[41]=data["Wood_deck_area_in_square_feet"]
    vector[42]=data["Open_porch_area_in_square_feet"]
    vector[43]=data["Enclosed_porch_area_in_square_feet"]
    vector[44]=data["Three_season_porch_area_in_square_feet"]
    vector[45]=data["Screen_porch_area_in_square_feet"]
    vector[46]=data["Pool_area_in_square_feet"]
    PoolQC=data["Pool_quality"]
    Fence=data["Fence_quality"]
    vector[49]=data["Value_of_miscellaneous_feature"]
    vector[50]=data["Month_Sold"]
    vector[51]=data["Year_Sold"] 
    MSZoning=data["MSZoning"]
    Street=data["Street"]
    Alley=data["Alley"]
    LandContour=data["LandContour"]
    Utilities=data["Utilities"]
    LotConfig=data["LotConfig"]
    LandSlope=data["LandSlope"]
    Neighborhood=data["Neighborhood"]
    Condition1=data["Condition1"]
    Condition2=data["Condition2"]
    BldgType=data["BldgType"]
    HouseStyle=data["HouseStyle"]
    RoofStyle=data["RoofStyle"]
    RoofMatl=data["RoofMatl"]
    Exterior1st=data["Exterior1st"]
    Exterior2nd=data["Exterior2nd"]
    MasVnrType=data["MasVnrType"]
    Foundation=data["Foundation"]
    Heating=data["Heating"]
    CentralAir=data["CentralAir"]
    Electrical=data["Electrical"]
    Functional=data["Functional"]
    GarageType=data["GarageType"]
    PavedDrive=data["PavedDrive"]
    MiscFeature=data["MiscFeature"]
    SaleType=data["SaleType"]
    SaleCondition=data["SaleCondition"]
    
    
    one_hot_list=columns.get("column").tolist()
    # print(one_hot_list)
    try:   
        MSZoning_index=one_hot_list.index("MSZoning_"+MSZoning)
        print(MSZoning_index)
        vector[MSZoning_index]=1 
    except:
        pass
    try:
        Street_index=one_hot_list.index("Street_"+Street)
        vector[Street_index]=1
    except:
        pass
    try:
        Alley_index=one_hot_list.index("Alley_"+Alley)
        vector[Alley_index]=1
    except:
        pass
    try:
        LandContour_index=one_hot_list.index("LandContour_"+LandContour)
        vector[LandContour_index]=1
    except:
        pass
    try:
        Utilities_index=one_hot_list.index("Utilities_"+Utilities)
        vector[Utilities_index]=1
    except:
        pass
    try:
        LotConfig_index=one_hot_list.index("LotConfig_"+LotConfig)
        vector[LotConfig_index]=1
    except:
        pass
    try:
        LandSlope_index=one_hot_list.index("LandSlope_"+LandSlope)
        vector[LandSlope_index]=1
    except:
        pass
    try:
        Neighborhood_index=one_hot_list.index("Neighborhood_"+Neighborhood)
        vector[Neighborhood_index]=1
    except:
        pass
    try:
        Condition1_index=one_hot_list.index("Condition1_"+Condition1)
        vector[Condition1_index]=1
    except:
        pass
    try:
        Condition2_index=one_hot_list.index("Condition2_"+Condition2)
        vector[Condition2_index]=1
    except:
        pass
    try:
        BldgType_index=one_hot_list.index("BldgType_"+BldgType)
        vector[BldgType_index]=1
    except:
        pass
    try:
        HouseStyle_index=one_hot_list.index("HouseStyle_"+HouseStyle)
        vector[HouseStyle_index]=1
    except:
        pass
    try:
        RoofStyle_index=one_hot_list.index("RoofStyle_"+RoofStyle)
        vector[RoofStyle_index]=1
    except:
        pass
    try:
        RoofMatl_index=one_hot_list.index("RoofMatl_"+RoofMatl)
        vector[RoofMatl_index]=1
    except:
        pass
    try:
        Exterior1st_index=one_hot_list.index("Exterior1st_"+Exterior1st)
        vector[Exterior1st_index]=1
    except:
        pass
    try:
        Exterior2nd_index=one_hot_list.index("Exterior2nd_"+Exterior2nd)
        vector[Exterior2nd_index]=1
    except:
        pass
    try:
        MasVnrType_index=one_hot_list.index("MasVnrType_"+MasVnrType)
        vector[MasVnrType_index]=1
    except:
        pass
    try:
        Foundation_index=one_hot_list.index("Foundation_"+Foundation)
        vector[Foundation_index]=1
    except:
        pass
    try:
        Heating_index=one_hot_list.index("Heating_"+Heating)
        vector[Heating_index]=1
    except:
        pass
    try:
        CentralAir_index=one_hot_list.index("CentralAir_"+CentralAir)
        vector[CentralAir_index]=1
    except:
        pass
    try:
        Electrical_index=one_hot_list.index("Electrical_"+Electrical)
        vector[Electrical_index]=1
    except:
        pass
    try:
        Functional_index=one_hot_list.index("Functional_"+Functional)
        vector[Functional_index]=1
    except:
        pass
    try:
        GarageType_index=one_hot_list.index("GarageType_"+GarageType)
        vector[GarageType_index]=1
    except:
        pass
    try:
        PavedDrive_index=one_hot_list.index("PavedDrive_"+PavedDrive)
        vector[PavedDrive_index]=1
    except:
        pass
    try:
        MiscFeature_index=one_hot_list.index("MiscFeature_"+MiscFeature)
        vector[MiscFeature_index]=1
    except:
        pass
    try:
        SaleType_index=one_hot_list.index("SaleType_"+SaleType)
        vector[SaleType_index]=1
    except:
        pass
    try:
        SaleCondition_index=one_hot_list.index("SaleCondition_"+SaleCondition)
        vector[SaleCondition_index]=1
    except:
        pass
       
    if LotShape:
        if LotShape=="Regular":
            vector[3]=3
        elif LotShape=="Slightly irregular":
            vector[3]=2
        elif LotShape=="Moderately Irregular":
            vector[3]=1
        else:
            vector[3]=0
    else:
        print("Pease enter the Lot Shape")
        
    if OverallQual:
        if OverallQual=="Very Excellent":
            vector[4]=10
        elif OverallQual=="Excellent":
            vector[4]=9
        elif OverallQual=="Very Good":
            vector[4]=8
        elif OverallQual=="Good":
            vector[4]=7
        elif OverallQual=="Above Average":
            vector[4]=6
        elif OverallQual=="Average":
            vector[4]=5
        elif OverallQual=="Below Average":
            vector[4]=4
        elif OverallQual=="Fair":
            vector[4]=3
        elif OverallQual=="Poor":
            vector[4]=2
        elif OverallQual=="Very Poor":
            vector[4]=1
    else:
        print("Enter the OverallQual")    
    if OverallCond:
        if OverallCond=="Very Excellent":
            vector[5]=10
        elif OverallCond=="Excellent":
            vector[5]=9
        elif OverallCond=="Very Good":
            vector[5]=8
        elif OverallCond=="Good":
            vector[5]=7
        elif OverallCond=="Above Average":
            vector[5]=6
        elif OverallCond=="Average":
            vector[5]=5
        elif OverallCond=="Below Average":
            vector[5]=4
        elif OverallCond=="Fair":
            vector[5]=3
        elif OverallCond=="Poor":
            vector[5]=2
        elif OverallCond=="Very Poor":
            vector[5]=1
    else:
        print("Enter the OverallQual")
    
    if ExterQual:
        if ExterQual=="Excellent":
            vector[9]=4
        elif ExterQual=="Good":
            vector[9]=3
        elif ExterQual=="Average":
            vector[9]=2
        elif ExterQual=="Fair":
            vector[9]=1
        else:
            vector[9]=0
    else:
        print("Enter the ExterQual")
    
    if ExterCond:
        if ExterCond=="Excellent":
            vector[10]=4
        elif ExterCond=="Good":
            vector[10]=3
        elif ExterCond=="Average":
            vector[10]=2
        elif ExterCond=="Fair":
            vector[10]=1
        else:
            vector[10]=0
    else:
        print("Enter the ExterQual")
    
    if BsmtQual:
        if BsmtQual=="Excellent":
            vector[11]=5
        elif BsmtQual=="Good":
            vector[11]=4
        elif BsmtQual=="Average":
            vector[11]=3
        elif BsmtQual=="Fair":
            vector[11]=2
        elif BsmtQual=="Poor":
            vector[11]=1
        else:
            vector[11]=0
    else:
        print("Enter the ExterQual")
    
    if BsmtCond:
        if BsmtCond=="Excellent":
            vector[12]=5
        elif BsmtCond=="Good":
            vector[12]=4
        elif BsmtCond=="Average":
            vector[12]==3
        elif BsmtCond=="Fair":
            vector[12]=2
        elif BsmtCond=="Poor":
            vector[12]=1
        else:
            vector[12]=0
    else:
        print("Enter the BsmtCond")
    
    if BsmtExposure:
        if BsmtExposure=="Good Exposure":
            vector[13]=4
        elif BsmtExposure=="Average Exposure":
            vector[13]=3
        elif BsmtExposure=="Mimimum Exposure":
            vector[13]=2
        elif BsmtExposure=="No Exposure":
            vector[13]=1
        else:
            vector[13]=0
    else:
        print("Enter the BsmtExposure")
    
    if BsmtFinType1:
        if BsmtFinType1=="Good Living Quarters":
            vector[14]=6
        elif BsmtFinType1=="Average Living Quarters":
            vector[14]=5
        elif BsmtFinType1=="Below Average Living Quarters":
            vector[14]=4
        elif BsmtFinType1=="Average Rec Room":
            vector[14]=3
        elif BsmtFinType1=="Low Quality":
            vector[14]=2
        elif BsmtFinType1=="Unfinshed":
            vector[14]=1
        else:
            vector[14]=0
    else:
        print("Enter the BsmtFinType1")
    
    if BsmtFinType2:
        if BsmtFinType2=="Good Living Quarters":
            vector[14]=6
        elif BsmtFinType2=="Average Living Quarters":
            vector[14]=5
        elif BsmtFinType2=="Below Average Living Quarters":
            vector[14]=4
        elif BsmtFinType2=="Average Rec Room":
            vector[14]=3
        elif BsmtFinType2=="Low Quality":
            vector[14]=2
        elif BsmtFinType2=="Unfinshed":
            vector[14]=1
        else:
            vector[14]=0
    else:
        print("Enter the BsmtFinType2")        
    if HeatingQC:
        if HeatingQC=="Excellent":
            vector[20]=4
        elif HeatingQC=="Good":
            vector[20]=3
        elif HeatingQC=="Average":
            vector[20]=2
        elif HeatingQC=="Fair":
            vector[20]=1
        else:
            vector[20]=0
    else:
        print("Enter the HeatingQC")
    if KitchenQual:
        if KitchenQual=="Excellent":
            vector[31]=4
        elif KitchenQual=="Good":
            vector[31]=3
        elif KitchenQual=="Average":
            vector[31]=2
        elif KitchenQual=="Fair":
            vector[31]=1
        else:
            vector[31]=0
    else:
        print("Enter the Kitchen quality") 
    
    if FireplaceQu:
        if FireplaceQu=="Excellent":
           vector[34]=5
        elif FireplaceQu=="Good":
           vector[34]=4
        elif FireplaceQu=="Average":
            vector[34]=3
        elif FireplaceQu=="Fair":
            vector[34]=2
        elif FireplaceQu=="Poor":
            vector[34]=1
        else:
            vector[34]=0
    else:
        print("Enter the FireplaceQu")
    
    if GarageFinish:
        if GarageFinish=="Finished":
            vector[36]=3
        elif GarageFinish=="Rough Finished":
            vector[35]=2
        elif GarageFinish=="Unfinished":
            vector[35]=1
        else:
            vector[35]=0
    else:
        print("Enter the Garage Finish")
    
    if GarageQual:
        if GarageQual=="Excellent":
            vector[39]=5
        elif GarageQual=="Good":
            vector[39]=4
        elif GarageQual=="Average":
            vector[39]=3
        elif GarageQual=="Fair":
            vector[39]=2
        elif GarageQual=="Poor":
            vector[39]=1          
        else:
            vector[39]=0
    else:
        print("Enter the GarageQual")    
    if GarageCond:
        if GarageCond=="Excellent":
            vector[40]=5
        elif GarageCond=="Good":
            vector[40]=4
        elif GarageCond=="Average":
            vector[40]=3
        elif GarageCond=="Fair":
            vector[40]=2
        elif GarageCond=="Poor":
            vector[40]=1          
        else:
            vector[40]=0
    else:
        print("Enter the GarageCond")         
    if PoolQC:
        if PoolQC=="Excellent":
            vector[47]=4
        elif PoolQC=="Good":
            vector[47]=3
        elif PoolQC=="Average":
            vector[47]=2
        elif PoolQC=="Fair":
            vector[47]=1         
        else:
            vector[47]=0
    else:
        print("Enter the PoolQC")   
    if Fence:
        if Fence=="Good Privacy":
            vector[48]=4
        elif Fence=="Minimum Privacy":
            vector[48]=3
        elif Fence=="Good Wood":
            vector[48]=2
        elif Fence=="Minimum Wood":
            vector[48]=1         
        else:
            vector[48]=0            
    raw_data1=pd.DataFrame({"columns":one_hot_list,"Reading":vector})
    raw_data1.to_csv("raw_data1.csv")
    result=model.predict([vector])
    
    return f"The prediction is {result[0]}"
    
    
if __name__=="__main__":
    app.run(debug=True)