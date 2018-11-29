package com.jongseol.agoodday.API;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.jongseol.agoodday.Model.Device;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;
import retrofit2.http.Query;

/**
 * @author jeje(las9897 @ gmail.com)
 * @file jongseol.agoodday.API.APIInterface.java
 * @brief Restful API. GET and POSt
 * @see Choice Data Type 1.List<Device> 2.JsonArray
 */
public interface APIInterface {


/**
 * @brief Request Method "GET": /posture/{device_id}
 *        Select * from posture_device where device_id = {device_id}
 * @param device_id
 * @return Call<List       <       Device>>
 *//*

        @GET("posture/{device_id}")
        Call<List<Device>> getDevice(@Path("device_id") String device_id);

        */
/**
 * @brief Request Method "GET": /posture/{device_id}?start_date={start_date}&end_date={end_date}
 *        Select * from posture_device where device_id = {device_id} and {start_date} <= date and date <= {end_date}
 * @param device_id
 * @param start_date
 * @param end_date
 * @return Call<List       <       Device>>
 *//*

        @GET("posture/{device_id}")
        Call<List<Device>> getDevice(@Path("device_id") String device_id, @Query("start_date") String start_date,
                        @Query("end_date") String end_date);
*/


    /**
     * @param device_id
     * @return Call<JsonArray>
     */

    @GET ( "device/{device_id}/" )
    Call<JsonArray> getDevice(@Path ( "device_id" ) String device_id);

    @GET ( "device/{device_id}/all" )
    Call<JsonArray> getPosture(@Path ( "device_id" ) String device_id);

    @Headers ( {"Accept: application/json", "Content-Type: application/json"} )
    @PATCH ("posture/{device_id}/update")
    Call<JsonArray> patchPosture(@Path("device_Id") String device_id, @Body JsonArray jsonArray);


    @FormUrlEncoded
    @PUT("posture/{device_Id}/update")
    Call<JsonObject> updatePosture(@Field("device_id") String device_id, @Field("date") String date, @Field("bad_count") int bad_couont,@Field("all_count") int all_count, @Field("ratio") float ratio);


}