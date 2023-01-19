<?php
class Crypto {
  // Properties
  private static string $ciphering;
  private static string $encryption_key; 
  private static int $options;
  private static bool $paramsSet = false;


  private final function  __construct() 
  {
       
  }

  public static function setParams (string $encryption_key, string $ciphering,int $options=0)
  {
    self::$encryption_key= $encryption_key;
    self::$ciphering = $ciphering;
    self::$options = $options;
    self::$paramsSet = true;

  }


  public static function encrypt(string $raw_data, string $iv)
  {

    if(self::$paramsSet == true)
    {
      $iv_length = openssl_cipher_iv_length(self::$ciphering);
      $encryption = openssl_encrypt($raw_data, self::$ciphering, self::$encryption_key, self::$options, $iv);
  
      return $encryption; 
    } 
    
    return NULL;

}

public  static function decrypt(string $encrypted_data,string $iv)
{


  if(self::$paramsSet == true)
  {
    $decryption = openssl_decrypt($encrypted_data, self::$ciphering, self::$encryption_key, self::$options, $iv);
    return $decryption;
  }


  return NULL;

}

}